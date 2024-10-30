# Table of Content
- [Table of Content](#table-of-content)
- [1. Project Name and Short Description](#1-project-name-and-short-description)
- [2. Installing / Usage / Getting Started](#2-installing--usage--getting-started)
  - [2.1 Install](#21-install)
  - [2.2 Usage](#22-usage)
  - [2.3 Getting Started](#23-getting-started)
- [3. Developing](#3-developing)
  - [3.1 Get the repository](#31-get-the-repository)
  - [3.2 How to Build](#32-how-to-build)
  - [3.3 How to Deploy](#33-how-to-deploy)
- [4. Features](#4-features)
- [5. Configuration](#5-configuration)
- [6. Contributing](#6-contributing)
- [7. References](#7-references)
- [8. Licensing](#8-licensing)

# 1. Project Name and Short Description

Project name: <enter your project name>

Description: <enter a project description here>

# 2. Installing / Usage / Getting Started

## 2.1 Install
Define the way the project within the repository needs to be installed.

## 2.2 Usage
Describe the basic usage of the project within the repository.
<!-- 
usage: phyton.exe dsBuildLogCrawler.py [-h] [-v] [-r RESULT] regex logfile [-d]

positional arguments:

  regex                      Single regular expression or file to filter in a log file
  logfile                    Filename that shall be filtered using the handed over regular expressions

options:

  -h, --help                 show this help message and exit
  -v, --version              show program's version, the author and the version's date
  -r RESULT, --result RESULT Filename for the results of the filtering
  -d                         plot out debug information

The script reads the <logfile> and searches with the help of the term(s) stated in <regex> for parts in the logfile that matches to the regular expression(s). The results are written into the <RESULT> and an exit value is put out depe
 -->
## 2.3 Getting Started
State additional things which needs to be done for a usage.

# 3. Developing

## 3.1 Get the repository

How can the repository be taken from the version controll system, e.g. `git clone https://github.com/tegepat/ds_build_log_crawler.git `

## 3.2 How to Build

Enter a description how the repository can be built, e.g.: 

<!-- Install the `pipenv` package using `pip install pipenv`. Create a new or recall an allready created virtual environment based on the pipenv using `pipenv shell`.

Included in the project are checks using pylint and ruff. Testing is done by pytest functions. -->

## 3.3 How to Deploy

Enter a description how the repository needs to deployed 

# 4. Features
Describe the features of project within the repository. 
<!-- 
This script searches Azure build step log file on build messages defined by one or more handed over regular expressions. The found results will be stored in a text file for further usage. Additional to this the script will output exit

* 0 success
* 1 the handed over regular expression file is empty
* 2 one or more handed over regular expressions are not compilable
* 4 the handed over log file does not exist
* 8 the handed over log file is empty
* 16 the handed over result file does not exist
* 32 the handed over resutl file is write protected

Additional non-core capabilities
 -->
# 5. Configuration
Describe possible configuration necessities.
<!-- ## Argument Regular Expression File and Path
* ArgType: `positional Argument`
* Type: `String`

Defines a single regular expression as search filter in the log file or a text file in which one or more regular expressions are defined. The single regular expressions are separated by a new line character in the file.

## Argument Log File Name and Path
* ArgType: `positional Argument`
* Type: `String`

Defines the log file which shall be processed with the regular expression(s) from .

## Argument Result File
* ArgType: `optional Argument`
* Type: `String`
* Label: `-r`
* Default: `./logmsgres.txt`

Name of the result file where the filter results will be stored to. There is a default name if a name is not stated.

## Argument Debug Level
* ArgType: `optional Argument`
* Type: `bool`
* Label: `-d`
* Default: `false`

Debug level of the script. 

## Version Argument
* ArgType: `optional Argument`
* Label: `-v, --version`

Shows the version information of the program

## Help Argument
* ArgType: `optional Argument`
* Label: `-h, --help`

Shows the help information of the program -->

# 6. Contributing
State the potential contribution to this repository.
<!-- 
For a new function or a found bug an Issue has to be created in the GitHub project repository (https://github.com/tegepat/ds_build_log_crawler.git). 

New development branches are created based on issues and end in a pull request back to the main branch. Please delete the development branch within the pull request process.

Every pull request shall lead to a new tag in main based on the current version number.
 -->
# 7. References
State potential references to other repositories/literature/web pages

# 8. Licensing

The licensing information and handling is not define till now and will be part of an additional development stage including an Issue.