# -*- coding: utf-8 -*-
from python_starter.template.core import Template

setup_body = '''#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

config = {{
    'name': '{name}',
    'author': '{author}',
    'author_email': '{author_email}',
    'url': '',
    'description': '',
    'long_description': open('README.rst', 'r').read(),
    'license': '{license}',
    'version': '0.0.1',
    'install_requires': [],
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "{license_classifiers}",
        "Development Status :: 1 - Planning",
    ],
    'packages': find_packages(),
}}

if __name__ == '__main__':
    setup(**config)
'''

setup_tmpl = Template(name='{name}/setup.py', body=setup_body)
