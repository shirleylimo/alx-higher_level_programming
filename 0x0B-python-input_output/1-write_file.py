#!/usr/bin/python3
"""
Module to define a function that returns number of lines in text file
"""


def write_file(filename="", text=""):
    """ Return number of characters in text file """
    with open(filename, "w", encoding="utf-8") as fd:
        return fd.write(text)
