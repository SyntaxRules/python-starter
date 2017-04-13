# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

import re
from setuptools import setup, find_packages

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('starter/starter.py').read(),
    re.M
).group(1)

setup(
    name="python-starter",
    packages=find_packages(),
    entry_points={
        "console_scripts": ['start_example = starter.__main__:main']
    },
    version=version,
    description="Python command line application bare bones template."
)
