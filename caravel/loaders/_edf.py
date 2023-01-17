# coding: utf-8
##########################################################################
# NSAp - Copyright (C) CEA, 2020
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
This module defines the edf dataset loader.
"""

# Third party import

# Package import
from .loader_base import LoaderBase


class EDF(LoaderBase):
    """ Define the mp4 loader.
    """
    allowed_extensions = [".edf"]

    def load(self, path):
        """ A method that load the edf data.
        """
        return 0

    def save(self):
        """ A method that save the image in edf.
        """
        return 0
