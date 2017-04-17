# Documentation

The documentation uses [mkdocs.org](http://mkdocs.org) to build and serve itself. This produces pretty HTML pages for external viewing and is compatible with ReadtheDocs.org.

To generate a PDF of this documentation use: https://github.com/jgrassler/mkdocs-pandoc

## Generating a PDF

To generate a PDF from mkdocs use [mkdocs-pandoc](https://github.com/jgrassler/mkdocs-pandoc).

To install it, perform the following steps:

1. yum install fonts-lmodern lmodern pandoc texlive-base texlive-latex-extra texlive-fonts-recommended texlive-latex-recommended texlive-xetex
2. yum install texlive-latex texlive-pdfpages texlive-pdftex



## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

.. Python-Starter documentation master file, created by
   sphinx-quickstart on Thu Apr 13 16:29:44 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Python-Starter's documentation!
==========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
