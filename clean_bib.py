import datetime
import sys
import os.path
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import *

if not len(sys.argv) == 3:
    print("Error. python clean_bib.py <input.bib> <output.bib>")

input_b = sys.argv[1]
output_b = sys.argv[2]

now = datetime.datetime.now()
print("{0} Cleaning duff bib records from {1} into {2}".format(now, input_b, output_b))

# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library
    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = page_double_hyphen(record)
    record = homogenize_latex_encoding(record)
    record_keys = list(record.keys())

    ## it deletes the keys that do not appear here.
    ## ENTRYTYPE AND ID are mandatory
    wanted = ["ENTRYTYPE", "ID","author", "journal", "number", "pages", "title", "volume", "year", "publisher"]
    record_unwanted = list(set(record_keys) - set(wanted))
    for val in record_unwanted:
        record.pop(val, None)
    return record


bib_database = None
with open(input_b) as bibtex_file:
    parser = BibTexParser()
    parser.customization = customizations
    parser.ignore_nonstandard_types = False
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
print("{0} Number of entries in inputfile: {1}".format(datetime.datetime.now(), len(bib_database.entries)))

if bib_database :
    now = datetime.datetime.now()
    success = "{0} Loaded {1} found {2} entries".format(now, input_b, len(bib_database.entries))
    print(success)
else :
    now = datetime.datetime.now()
    errs = "{0} Failed to read {1}".format(now, input_b)
    print(errs)
    sys.exit(errs)


# Now, the output file existence is check. If it exist, entries are not update
# only new entries are inserted in output file.
if os.path.isfile(output_b):
    print("{0} Exists {1}".format(datetime.datetime.now(), output_b))
    with open(output_b) as new_bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        parser.ignore_nonstandard_types = False
        new_bib_database = bibtexparser.load(new_bibtex_file, parser=parser)
    print("{0} Number of entries in outputfile: {1}".format(datetime.datetime.now(), len(bib_database.entries)))
    cont = 0
    for entry_input in bib_database.entries:
            find = False
            for entry_output in new_bib_database.entries:
                if entry_input["ID"] == entry_output["ID"]:
                    find = True
                    break

            if not find:
                cont += 1
                new_bib_database.entries.append(entry_input)
    print("{0} Number of new entries: {1}".format(datetime.datetime.now(), cont))

else:
    new_bib_database = bib_database

# Write output file file
bibtex_str = None
if new_bib_database:
    writer = BibTexWriter()
    writer.order_entries_by = ('author', 'year', 'type')
    bibtex_str = bibtexparser.dumps(new_bib_database, writer)
    #print(str(bibtex_str))
    with open(output_b, "w") as text_file:
        print(bibtex_str, file=text_file)

if bibtex_str:
        print("{0} Number of total entries: {1}".format(datetime.datetime.now(), len(new_bib_database.entries)))
else:
    now = datetime.datetime.now()
    errs = "{0} Failed to write {1}".format(now, output_b)
    print(errs)
    sys.exit(errs)
