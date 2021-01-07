# Duolingo Podcast Transcript Downloader

This is a simple Python script to automatically find all episodes for a given 
language and download the transcript for each one as a PDF.

### How to use

1. Clone this repo
2. Create a virtual environment
3. Install requirements `pip install -r requirements.txt`
4. Install `wkhtmltopdf` dependency for `pdfkit`. See [here](https://wkhtmltopdf.org/downloads.html).
5. Update `WKHTLMTOPDF_PATH` to match wherever you installed `wkhtmltopdf`
6. Run `main.py`

Files will be saved in `./output` unless you change `OUTPUT_PATH`.

### Changing Language

Change `LANGUAGE` in `main.py` to either `spanish`, `french` or `english`. 

_Note:_ This script has only been tested with `spanish`.


### Note

You may seem some error messages near the end. I haven't investigated them because 
it seems like all transcripts downloaded successfully. It's probably `pdfkit`
freaking out about an embedded video or other un-PDF-able elements.
