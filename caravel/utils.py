###############################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
###############################################################################


"""
This module provides common utilities.
"""

# Imports
import re
from docx import Document


def export_report(report, timestamp, outfile):
    """ Export the report in docx format.

    Parameters
    ----------
    report: str
        a dictionary with recursive keys and values.
    timestamp: str
        a timestamp.
    outfile: str
        the path to the generated docx file.
    """
    document = Document()
    section = document.sections[0]
    header = section.header
    paragraph = header.paragraphs[0]
    paragraph.text = "NeuroSpin\tReporting\t{0}".format(timestamp)
    paragraph = document.add_paragraph(
        "\n\n\n\nYou will find below the report generated the "
        "'{0}'. If you have any questions please use the contact mail: "
        "rlink@cea.fr.".format(timestamp))
    for family, family_item in report.items():
        document.add_heading(family.replace(".", " ").title())
        for validator, validator_item in family_item.items():
            split_validator = re.findall("[A-Z][^A-Z]*", validator)
            document.add_heading(" ".join(split_validator))
            paragraph = document.add_paragraph(
                "\n\n Below the table summarizing the errors.\n\n")
            for key, values in validator_item.items():
                table = document.add_table(rows=len(values), cols=2)
                cell = table.cell(0, 0)
                cell.text = key
                for idx, val in enumerate(values):
                    cell = table.cell(idx, 1)
                    cell.text = val
    document.save(outfile)
