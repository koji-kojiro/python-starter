# -*- coding: utf-8 -*-
import os
import sys
import argparse
import subprocess
from python_starter.core import Project
from python_starter.template.license_tmpl import candidate
from python_starter import __version__


class PythonStarterParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, 'try \'{} --help\'\n'.format(self.prog))


class PythonStarterFormatter(argparse.RawTextHelpFormatter):
    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append(option_string)
                parts[-1] += '={}'.format(args_string)
            return ', '.join(parts)

    def _format_args(self, action, default_metavar):
        get_metavar = self._metavar_formatter(action, default_metavar)
        if action.nargs is None:
            result = '{0:s}'.format(*get_metavar(1))
        elif action.nargs == argparse.OPTIONAL:
            result = '{0:s}'.format(*get_metavar(1))
        elif action.nargs == argparse.ZERO_OR_MORE:
            result = '[{0:s}...]'.format(*get_metavar(2))
        elif action.nargs == argparse.ONE_OR_MORE:
            result = '{0:s}...'.format(*get_metavar(2))
        elif action.nargs == argparse.REMAINDER:
            result = '...'
        elif action.nargs == argparse.PARSER:
            result = '{0:s}...'.format(*get_metavar(1))
        else:
            formats = ['{0:s}' for _ in range(action.nargs)]
            result = ' '.join(formats).format(*get_metavar(action.nargs))
        return result


class ListLicensesAction(argparse._HelpAction):
    def __call__(self, parser, *args, **kwargs):
        print(', '.join(candidate.keys()))
        parser.exit()


class PythonStarter(object):
    def __init__(self):
        try:
            author = subprocess.check_output(
                'git config --get user.name'.split()).rstrip()
            email = subprocess.check_output(
                'git config --get user.email'.split()).rstrip()
            self.git_enabled = True
        except:
            author = ''
            email = ''
            self.git_enabled = False

        self.parser = PythonStarterParser(
            prog='python-starter',
            add_help=False,
            usage='%(prog)s [options] target',
            formatter_class=PythonStarterFormatter)
        self.parser._optionals.title = 'options'
        self.parser.add_argument(
            'name', type=str, metavar='target', help=argparse.SUPPRESS)
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
            help='license (default: MIT)',
            default='MIT')
        self.parser.add_argument(
            '--list',
            action=ListLicensesAction,
            help='list available licenses')
        self.parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s {version}'.format(version=__version__))
        self.parser.add_argument(
            '--help', action='help', help='show this message and exit\n ')

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
    cli = PythonStarter()
    cli.run()


if __name__ == '__main__':
    main()
