"""Configuration for pytest.

Longer description of this module.
"""

__author__ = "One solo developer"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "mail@example.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "YYYY/MM/DD"
__deprecated__ = False
__email__ = "mail@example.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

################################################################################
# Imports

import pytest


################################################################################
# Variables
@pytest.fixture()
def example_data():
    """State as example of a data fixture."""
    return [1, 2, 3, 4]


################################################################################
# Functions

################################################################################
# Classes

############################################################################
# Member Functions
