# utils.py
# pylint: disable=unused-import


""" 
Common utilities and imports for Jeff's projects
"""

import datetime
import re
from typing import Literal
from typing import TypeVar
from collections import Counter
import subprocess

from dateutil import parser

T = TypeVar("T")  # Generic type


# def formatted_date(input_date) -> str:
#     """Returns the input date in YYYY-MM-DD format."""
#     return datetime.datetime(input_date).strftime("%Y-%m-%d")


def current_date() -> str:
    """Returns the current date in YYYY-MM-DD format."""
    return datetime.datetime.now().strftime("%Y-%m-%d")


def current_time() -> str:
    """Returns the current time in HH:MM:SS format."""
    return datetime.datetime.now().strftime("%H:%M:%S")


def current_datetime() -> str:
    """Returns the current date and time in YYYY-MM-DD HH:MM:SS format."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def startup():
    """
    Startup on every invocation:
    Clears the terminal
    Prints the date/time of the current run & a blank line
    """
    subprocess.call('cls', shell=True)
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d ..... %H:%M:%S")
    print("START at", formatted_time, "\n")


def standardize_date_dateutil(date_string):
    """
Trys to convert variouos formats of Date Strings to YYYY-MM-DD format
Usage
    print(standardize_date_dateutil("10-27-2023"))
    print(standardize_date_dateutil("10-27-23"))
    print(standardize_date_dateutil("2023-10-27"))
    print(standardize_date_dateutil("23-10-27"))
    print(standardize_date_dateutil("invalid date"))
    """
    try:
        date_obj = parser.parse(date_string).date()
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        return None
