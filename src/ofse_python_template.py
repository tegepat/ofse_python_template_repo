"""
OFSE Python Template Repository.

This script acts as a Python script file template.

The information contained herein is confidential property of Baker Hughes Company.
The use, copying, transfer or disclosure of such information is prohibited except
by express written agreement with Baker Hughes Company.
"""

__author__ = "John Doe"
__authors__ = ["John Doe", "And another one", "etc"]
__contact__ = "john.doe@bakerhughes.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "2024/10/29"
__deprecated__ = False
__email__ = "john.doe@bakerhughes.com"
__license__ = "Baker Hughes"
__maintainer__ = "developer"
__status__ = "Draft"
__version__ = "0.0.1"

###################################################################################################
# Imports

import argparse
import logging
import logging.config

from check_arguments import check_arguments

###################################################################################################
# Variables (always in capitals)


###################################################################################################
# Functions


def parse_arguments(arglist: list[str] | None, logger: logging.Logger) -> list[str]:
    """
    Parse command line arguments.

    Parameters
    ----------
    arglist: list[str]
        List of strings to parse
    logger: logging.Logger
        Logging object

    Returns
    -------
    args: list
        parsed arguments list

    """
    logger.debug("Enter parsargs function")
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="version: "
        + __version__
        + ", author: "
        + __author__
        + ", date: "
        + __date__,
        help="show program's version, the author and the version's date",
    )
    parser.add_argument(
        "regex", help="Single regular expression to check in a log file"
    )
    parser.add_argument("-d", "--debug", action="store_true", help=argparse.SUPPRESS)

    args = parser.parse_args(arglist)

    if args.debug:  # pragma: no cover
        logger.setLevel(logging.DEBUG)

    logger.debug("Arguments are: %s", args)

    return args


def main(arglist: list[str] | None = None) -> None:
    """
    Run the main functionality of this module.

    Parameters
    ----------
    arglist : list[str] | None, optional
        List of strings to hold the argument list for testing
        (see: https://pythontest.com/testing-argparse-apps/), by default None

    """
    # Get an logger object
    logger: logging.Logger = logging.getLogger(__name__)
    # config the logger object
    logging.basicConfig(
        filename="logger.log",
        encoding="utf-8",
        format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s",
        datefmt="%a, %d %b %Y - %H:%M:%S %z",
        level=logging.WARNING,
    )

    # Get the arguments from the command line
    args = parse_arguments(arglist, logger)

    # Check the arguments handed over
    regexlist = check_arguments(args, logger)

    print(f"Regular expression list is {regexlist}")

    # shutdown the logging system regularly
    logging.shutdown()


###################################################################################################
# Scripts
if __name__ == "__main__":
    main()
