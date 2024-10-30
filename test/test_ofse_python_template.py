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

def preptest():
    """Prepare the test run."""
    resfile = "./logmsgres.txt"
    if os.path.exists(resfile):
        os.remove(resfile)
    open("./testdata/resempty.txt", "w").close()


def test_shlex():
    """Test the shlex funtionality used in the different test scenarios."""
    # I want to write this
    command = r'"(\S*):(\d+):(\d+): [iInNfFoO|wWaArRnNiInNgG|eErR{2}oOrR|nNoOtTeE]+: (\d+):( \S+)+" -d'

    # command parsers want this
    as_list = [
        r"(\S*):(\d+):(\d+): [iInNfFoO|wWaArRnNiInNgG|eErR{2}oOrR|nNoOtTeE]+: (\d+):( \S+)+",
        "-d",
    ]

    # shlex.split() does the work for me
    assert shlex.split(command) == as_list


test_cases = [
    (
        '"(\S*):(\d+):(\d+): [iInNfFoO|wWaArRnNiInNgG|eErR{2}oOrR|nNoOtTeE]+: (\d+):( \S+)+" -d',
        "Regular expression list is ['(\\\\S*):(\\\\d+):(\\\\d+): [iInNfFoO|wWaArRnNiInNgG|eErR{2}oOrR|nNoOtTeE]+: (\\\\d+):( \\\\S+)+']",
    ),  # only positional args
    (
        "./testdata/regexcont.txt -d",
        "Regular expression list is ['^{\\\\S}+$\\n', '(\\\\S*):(\\\\d+):(\\\\d+): [iInNfFoO|wWaArRnNiInNgG|eErR{2}oOrR|nNoOtTeE]+: (\\\\d+):( \\\\S+)+']",
    ),  # all normal args with regex in file
]


@pytest.mark.parametrize("command, expected_output", test_cases)
def test_argparseValidArguments(capsys, command, expected_output):
    """
    Test function to test the script's normal behavior.

    Parameters
    ----------
    capsys : pytest fixture
        Captures the stdout and stderr output during the execution of test functions
    command : str
        String with input arguments
    expected_output : str
        The expected output of the program based on the command
    """
    preptest()
    main(shlex.split(command))
    captured = capsys.readouterr()
    output = captured.out + captured.err
    assert expected_output in output


test_cases_sys_exit = [
    ("", "error: the following arguments are required: regex"),  # no args
    ("'^{\S}+$' -g", "error: unrecognized arguments: -g"),  # wrong optional arg
    (
        "'^{\S}+$' -",
        "error: unrecognized arguments: -",
    ),  # non-valid optional arg
    (
        "'^(test+$'",
        "error: the regular expression ^(test+$ throws an error",
    ),  # the handed over regex is not compilable
    (
        "'^test)+$'",
        "error: the regular expression ^test)+$ throws an error",
    ),  # othe handed over regex is not compilable
]


@pytest.mark.parametrize("command, expected_output", test_cases_sys_exit)
def test_main(capsys, command, expected_output):
    """
    Test function for checking the argparse functionality with SystemError.

    Parameters
    ----------
    capsys : pytest fixture
        Captures the stdout and stderr output during the execution of test functions
    command : str
        String with input arguments
    expected_output : str
        The expected output of the program based on the command
    """
    with pytest.raises(SystemExit):  # Expecting SystemExit due to argparse error
        main(shlex.split(command))
    captured = capsys.readouterr()  # Capture both stdout and stderr
    output = captured.out + captured.err  # Combine stdout and stderr
    assert expected_output in output