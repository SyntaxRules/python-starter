# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 <company or person>
#
"""
setup.py: For installing via pip
"""

import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('starter/starter.py').read(),
    re.M
).group(1)

setup(
    name="python-starter",
    version=version,
    description="Python command line application targeted toward open source best practices.",
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    entry_points={
        "console_scripts": ['start_example = starter.__main__:main']
    },
    test_suite='tests',
    tests_require=['coverage',
                   'pytest',
                   'pylint',
                   'mock']
)
