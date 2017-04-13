# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
"""
The entry point for this application.
"""
from __future__ import print_function

__version__ = "0.2.0"


class StartExample(object):
    """
    A example class that is the starts this application
    """

    def __init__(self):
        self.location = "World"

    def run(self):
        self.print_version()
        print("Hello {}!".format(self.location))

    def print_version(self):
        print("Version: {}".format(__version__))
