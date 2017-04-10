# -*- coding: utf-8 -*-
import os
import datetime
from template.core import Template
from template.license_tmpl import choose
from template.setup_tmpl import setup_tmpl
from template.gitignore_tmpl import gitignore_tmpl


class Project(object):
    def __init__(self,
                 name='name',
                 author='author',
                 author_email='author_email',
                 licence='MIT'):
        license_info = choose(licence)
        self.params = {
            'name': os.path.dirname(name + '/'),
            'author': author,
            'author_email': author_email,
            'license': licence,
            'license_classifiers': license_info['classifiers_text'],
            'year': datetime.date.today().year,
        }
        # {name}/setup.py
        self.setup = setup_tmpl
        # {name}/README.rst
        self.readme = Template(
            name='{name}/README.rst', body='{name}\n--------\n')
        # {name}/.gitignore
        self.gitignore = gitignore_tmpl
        # {name}/{name}/__init__.py
        self.module = Template(name='{name}/{name}/__init__.py', body='')
        # {name}/LICENSE
        self.licence = license_info['template']

    def make(self):
        self.setup.make(**self.params)
        self.readme.make(**self.params)
        self.gitignore.make(**self.params)
        self.module.make(**self.params)
        self.licence.make(**self.params)
