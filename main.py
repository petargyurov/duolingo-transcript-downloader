import os
import threading

import pdfkit
import requests
from bs4 import BeautifulSoup

WKHTLMTOPDF_PATH = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
BASE_URL = "https://podcast.duolingo.com/"
LANGUAGE = "spanish"  # spanish, french or english
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=WKHTLMTOPDF_PATH)
OUTPUT_PATH = "output"


def get_page_count():
    base_page = requests.get(f"{BASE_URL}/{LANGUAGE}.html")
    soup = BeautifulSoup(base_page.text, 'html.parser')
    paginator = soup.find(attrs={'class': 'paginator'})
    return int(paginator.text.split('/')[1][1:3])


def get_episode_urls(page_index):
    url = f"{BASE_URL}/{LANGUAGE}{page_index}.html"
    if page_index == 1:
        url = f"{BASE_URL}/{LANGUAGE}.html"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    episodes = soup.find_all('article')
    for e in episodes:
        episode_urls.append(e.find('a').get('href')[2:])


def download_pdf(episode_slug):
    try:
        pdfkit.from_url(
            url=f"{BASE_URL}/{episode_slug}",
            output_path=f"./{OUTPUT_PATH}/{episode_slug}.pdf",
            configuration=PDFKIT_CONFIG,
            options={'margin-top'   : '1cm',
                     'margin-bottom': '1cm',
                     'margin-right' : '2cm',
                     'margin-left'  : '2cm'})
    except Exception as e:
        print(f"Something went wrong whilst downloading PDF for episode {episode_slug}. Error: {e}")


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_PATH):
        os.makedirs('output')

    total_pages = get_page_count()
    episode_urls = []

    for p in range(1, total_pages+1):
        print(f"Getting episode links on page {p}...")
        get_episode_urls(page_index=p)

    print(f"Found {len(episode_urls)} episodes...")

    for episode in episode_urls:
        print(f"Starting PDF download for episode {episode}...")
        thread = threading.Thread(target=download_pdf, args=(episode,),
                                  daemon=False)
        thread.start()
