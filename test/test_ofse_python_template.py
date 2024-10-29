"""
Test file for the ofse_python_template script.

The information contained herein is confidential property of Baker Hughes Company.
The use, copying, transfer or disclosure of such information is prohibited except
by express written agreement with Baker Hughes Company.
"""

__author__ = "Jane Doe"
__authors__ = ["Jane Doe", "And another one", "etc"]
__contact__ = "jane.doe@bakerhughes.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "2024/10/29"
__deprecated__ = False
__email__ = "jane.doe@bakerhughes.com"
__license__ = "Baker Hughes"
__maintainer__ = "developer"
__status__ = "Draft"
__version__ = "0.0.1"

################################################################################
# Imports

import os
import shlex

from conftest import example_data
import pytest

from ofse_python_template import main
import filecmp

################################################################################
# Variables


################################################################################
# Functions