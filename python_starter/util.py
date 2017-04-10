# -*- coding: utf-8 -*-
import os
import argparse
import subprocess
from core import Project
from template.license_tmpl import candidate


class CLI(object):
    def __init__(self):
        try:
            author = subprocess.check_output(
                'git config --get user.name'.split()).rstrip()
            email = subprocess.check_output(
                'git config --get user.email'.split()).rstrip()
            self.git_enabled = True
        except:
            print('git is not enabled')
            author = ''
            email = ''
            self.git_enabled = False

        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        self.parser.add_argument('name', type=str, help='project name')
        self.parser.add_argument(
            '--author',
            type=str,
            metavar='author',
            nargs='?',
            help='author name (default: git user.name)',
            default=author)
        self.parser.add_argument(
            '--email',
            type=str,
            metavar='email',
            dest='author_email',
            nargs='?',
            help='author email (default: git user.email)',
            default=email)
        self.parser.add_argument(
            '--license',
            type=str,
            metavar='license',
            dest='licence',
            nargs='?',
            choices=candidate.keys(),
            help='license (default: MIT)\n{}'.format(candidate.keys().__str__(
            )),
            default='MIT')

    def run(self):
        args = self.parser.parse_args().__dict__
        project = Project(**args)
        project.make()
        if self.git_enabled:
            with open(os.path.devnull, 'w') as fp:
                subprocess.call(
                    'git init {}'.format(args['name']).split(),
                    stdout=fp,
                    stderr=subprocess.STDOUT)


def main():
    cli = CLI()
    cli.run()


if __name__ == '__main__':
    main()
