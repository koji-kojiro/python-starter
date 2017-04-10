#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from python_starter import __version__

config = {
    'name': 'python-starter',
    'author': 'Kojiro TANI',
    'author_email': 'kojiro0531@gmail.com',
    'url': 'https://github.com/koji-kojiro/python-starter',
    'description': '\'module-starter\' for Python',
    'long_description': open('README.rst', 'r').read(),
    'license': 'MIT',
    'version': __version__,
    'install_requires': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Environment :: Console",
        "Development Status :: 4 - Beta",
    ],
    'packages': find_packages(exclude=['example', ]),
    'entry_points':
    '[console_scripts]\npython-starter=python_starter.util:main'
}

if __name__ == '__main__':
    setup(**config)
