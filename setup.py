# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open('README.md') as readme_file:
    readme = readme_file.file()


setuptools.setup(
    name="badapy",
    version="0.1",
    author="Tim Kreitner",
    author_email="tim@kreitner.xyz",
    description="A python package implementation of the EUROCONTROL BADA calculationse.",
    classifiers=['Programming Language :: Python :: 3.6',
                 'Development Status :: Beta'],
    url="https://github.com/tabassco/badapy",
    packages=setuptools.find_packages(),
    python_reqires='>=3.5',
    install_requires=[
        'pandas',
        'numpy',
        'scipy'
    ]
)

