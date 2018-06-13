# clean_bib.py - Delete Unwanted Bibliography fields from .bib files.

Do you use Mendeley, Papers, Zotero or other bibliographic softwares that export their bibliography to bibtex .bib files for use in LaTeX with BibTeX or bibLaTeX? 

Do you hate the way those bibliographic softwares generally export a .bib file that can’t exclude certain fields and so make a total ugly hash of your Bibliography Entries?

If so, then this Python script is for you! It deletes the extraneous fields in the .bib file leaving you with just the essential ones, like Author, Year, Title, Journal, etc. 

Never have a horrid bibliography entry with the article Abstract (!) copied into it every again! No more hashing about with .csl files ever again (not that .bibtex and .biblatex support those horrid things anyway).

## Installing the script

You will need Python 3. I use Python 3.3 - I haven’t checked if this works with Python 2.x. In fact, I know it won’t. Use Python 3 or convert it to Python 2 yourself.

You will also need the super-excellent [BibTexParser project](https://bibtexparser.readthedocs.org/en/latest/index.html) installed into your Python environment. If you don’t have that installed, install like this:

    pip install bibtexparser

Otherwise see the instructions on the linked page above if you don’t/can’t/won’t use pip.

## Using the script

To run the script, on the command line, type:

    python clean_bib.py <input.bib> <output.bib>

## Customising what fields are removed

It works by removing fields you don’t want, and leaving any others. You can customise what fields are removed by editing the line:

    unwanted = ["doi", "url", "abstract", "file", "isbn", "link", "keyword", "mendeley-tags", "annote", "pmid", "chapter", "institution", "issn", "month"]

Just add any fields you don’t want to this Python list. If you desire a field that’s being deleted, e.g., doi, url, isbn, etc., then remove it from the list.

## Updating output.bib
If the output.bib file exists before running the script, the old entries are kept in the file. Only new entries will add in the output.bib. So, if you change any field in the output.bib file, 
these changes will be kept.

## WARRANTY

aahahahahahahahahahaha No. None. Nada. Nihil. Use at your own risk.


