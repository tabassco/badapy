# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="badapy",
    version="0.1",
    author="Tim Kreitner",
    author_email="tim@kreitner.xyz",
    description="A python package implementation of the EUROCONTROL BADA calculationse.",
    classifiers=["Programming Language :: Python :: 3.7", "Development Status :: Beta"],
    url="https://github.com/tabassco/badapy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_reqires=">=3.7",
    install_requires=["pandas", "numpy", "scipy"],
)
