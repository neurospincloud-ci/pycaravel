"""
BIDS directory parsing (user mode)
==================================

Credit: A Grigis

pycaravel is a Python package that enables you to parse various source of data.
In this tutorial you will learn how to parse and search in a BIDS directory.

First checks
------------

In order to test if pycaravel package is installed on your machine, you can
check the package version.
"""

import caravel

print(caravel.__version__)

#############################################################################
# Now you can run the the configuration info function to see if all the
# dependencies are installed properly:

print(caravel.info())

#############################################################################
# Create a parser for your project
# --------------------------------
#
# The package provides a common interface to parse a BIDS directory. The
# parsing rules are defined by projects in the module, so we will beed to
# specify the project name you are working on. For the moement it is not
# possible to specify these rules via the API.

parser = caravel.Caravel(
    project="hbn",
    layoutdir="/neurospin/tmp/pycaravel/layout")

#############################################################################
# You can now list the available configurations for your project, and the
# available layout representations pre-generated. Note that these
# representations are sorted by dates, and that the latest one will be used.

from pprint import pprint

pprint(parser.conf)
pprint(parser.representation)

#############################################################################
# You can export the whole 'sourcedata' layout in a pandas DataFrame.

print(parser.export_layout("sourcedata"))

#############################################################################
# It is also possible to filter this dataset. You need first to list all the
# avaliable filtering keys, then list all the availables values for the
# filtering key(s) of interest, and finally filter your dataset.

print(parser.list_keys("sourcedata"))
print(parser.list_values("sourcedata", "subject"))
print(parser.list_values("sourcedata", "modality"))
search1 = parser.filter_layout("sourcedata", subject="S01",
                               modality="anat|func")
print(search1)
search2 = parser.filter_layout("sourcedata", extensions="tsv")
print(search2)

#############################################################################
# Finally you may want to ask the system to load the filtered data. Only a
# couple of file extensions are supported. If no loader has been found the
# filename is returned
data1 = parser.load_data("sourcedata", search1)
pprint(data1)
data2 = parser.load_data("sourcedata", search2)
pprint(data2)




