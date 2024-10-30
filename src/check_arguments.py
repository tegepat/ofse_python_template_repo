"""
Command line interface arguments checking.

This script searches for build messages in Azure build pipeline log files.

The information contained herein is confidential property of Baker Hughes Company.
The use, copying, transfer or disclosure of such information is prohibited except
by express written agreement with Baker Hughes Company.
"""

__author__ = "Patrik Tegetmeier"
__authors__ = ["Patrik Tegetmeier", "And another one", "etc"]
__contact__ = "patrik.tegetmeier@bakerhughes.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "2024/07/26"
__deprecated__ = False
__email__ = "patrik.tegetmeier@bakerhughes.com"
__license__ = "Baker Hughes"
__maintainer__ = "developer"
__status__ = "Release"
__version__ = "1.0.0"

###################################################################################################
# Imports

import logging
import logging.config
import os.path
import re


###################################################################################################
# Variables (always in capitals)

SUCCESS: int = 0
RE_FILE_EMPTY: int = 1
RE_CRASH: int = 2
LOG_FILE_NOT_EXIST: int = 4
LOG_FILE_EMPTY: int = 8
RES_FILE_NOT_EMPTY: int = 16
RES_FILE_WRITE_PROTECTED: int = 32


###################################################################################################
# Functions


def check_regex(regex: str, logger: logging.Logger) -> bool:
    """
    Check if the handed over string is a valid Python regular expression string.

    Parameters
    ----------
    regex : str
        The assumable regular expression string
    logger: logging.Logger
        Logging object

    Returns
    -------
    bool :
        True if the handed over string is a valid Python regular expression

    """
    logger.debug("Enter check_regex function")
    try:
        re.compile(regex)
    except Exception as exc:
        fstring = f"error: the regular expression {regex} throws an error"
        print(fstring)
        logger.error("error: the regular expression %s throws an error", regex)
        raise SystemExit(RE_CRASH) from exc

    return True


def check_file_content(file: str, logger: logging.Logger) -> list[str]:
    """
    Check if the file contains a list of strings which represents regular expressions.

    Parameters
    ----------
    file : str
        The file containing regular expressions.
    debug : bool
        debug flag
    logger: logging.Logger
        Logging object

    Returns
    -------
    list : str
        The list of regular expressions.

    """
    logger.debug("Enter checkfilecontent function")
    relist: list[str] = []
    recount: int = 0

    with open(file, encoding="utf-8") as f:
        for line in f.readlines():
            if check_regex(line, logger) is True:
                relist.append(line)
                recount = recount + 1

    logger.debug("Number of regular expressions found: %d", recount)

    return relist


def check_file_not_empty(file: str) -> bool:
    """
    Check if the handed over file is not empty.

    Parameters
    ----------
    file : str
        File name to check on emptyness

    Returns
    -------
    bool
        True if file is not empty, otherwise False
    """
    ret: bool = False
    if os.path.getsize(file) != 0:
        ret = True

    return ret


def check_existens(file: str) -> bool:
    """
    Check if the handed over element is a file.

    Parameters
    ----------
    file : str
        file including path to check

    Returns
    -------
    bool
        True if element is a file, else False
    """
    ret: bool = False
    if os.path.isfile(file) is True:
        ret = True

    return ret


def check_regex_file(reg: str, logger: logging.Logger) -> list[str]:
    """
    Check the regex argument.

    Check if regex argument is a file or a regex string and if a file is handed
    over it is checked if this file is empty.

    Parameters
    ----------
     reg : str
        regex argument which hold a regex or a file with regexs
    logger : logging.Logger
        Logging object

    Returns
    -------
    list[str]
        _list of the regular expressions which shall be the filter for the log file
    """
    logger.debug("Enter check_regex_file function")
    # f-String for handling the System Exit
    fstring: str = ""
    # regex result listing
    relist: list[str] = []

    # check if the regex argument is a file or a direct regex
    if check_existens(reg) is True:
        # check if the regex file is not empty
        if check_file_not_empty(reg) is True:
            relist = check_file_content(reg, logger)
            logger.debug("multiple regex defined %s", relist)
        else:
            fstring = f"error: the regex file: {reg} is empty"
            print(fstring)
            logger.error("error: the regex file is empty %s", reg)
            raise SystemExit(RE_FILE_EMPTY)
    elif check_regex(reg, logger) is True:
        # take over the regex if it is a direct regex string
        relist.append(reg)
        logger.debug("single regex defined %s", relist)

    return relist


def check_arguments(args: list[str], logger: logging.Logger) -> list[str]:
    """
    Check the file states of the input arguments files.

    Parameters
    ----------
    args : list[str]
        list of the input arguments
    logger: logging.Logger
        Logging object

    Returns
    -------
    list[str]
        list of the regular expressions which shall be the filter for the log file
    """
    logger.debug("Enter check_arguments function")
    # regex result listing
    relist: list[str] = []

    # check regex file if handed over and get regular expression to a list
    relist = check_regex_file(args.regex, logger)

    return relist
