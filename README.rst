python-starter
==============

| |MIT License| |python| |PyPI|
| *'module-starter'* for Python.

Requirements
------------

-  python >= (2.6, 3.3)

Installation
------------

::

    $ pip install python-starter

Usage
-----

::

    $ python-starter --help
    usage: python-starter [options] target

    options:
      --author=author    author name (default: git user.name)
      --email=email      author email (default: git user.email)
      --license=license  license (default: MIT)
      --list             list available licenses
      --version          show program's version number and exit
      --help             show this message and exit
                          

Example
-------

::

    $ git config --get user.name
    foo
    $ git config --get user.email
    foo@bar.com
    $ python-starter example

`example/setup.py <https://github.com/koji-kojiro/python-starter/blob/master/example/setup.py>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from setuptools import setup, find_packages

    config = {
        'name': 'example',
        'author': 'foo',
        'author_email': 'foo@bar.com',
        'url': '',
        'description': '',
        'long_description': open('README.rst', 'r').read(),
        'license': 'MIT',
        'version': '0.0.1',
        'install_requires': [],
        'classifiers': [
            "Programming Language :: Python",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Development Status :: 1 - Planning",
        ],
        'packages': find_packages(),
    }

    if __name__ == '__main__':
        setup(**config)

`example/LICENSE <https://github.com/koji-kojiro/python-starter/blob/master/example/LICENSE>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    MIT License

    Copyright (c) 2017 foo

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

`example/README.rst <https://github.com/koji-kojiro/python-starter/blob/master/example/README.rst>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: rest

    example
    --------

`example/.gitignore <https://github.com/koji-kojiro/python-starter/blob/master/example/.gitignore>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    __pycache__/
    *.py[cod]
    *$py.class
    *.so
    .Python
    env/
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    *.egg-info/
    .installed.cfg
    *.egg
    .python-version
    .env
    venv/
    ENV/

License
-------

Distributed under `MIT
License <https://github.com/koji-kojiro/python-starter/blob/master/LICENSE>`__.

Author
------

`Kojiro TANI <https://github.com/koji-kojiro>`__ (kojiro0531@gmail.com)

.. |MIT License| image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/koji-kojiro/python-starter/blob/master/LICENSE
.. |python| image:: https://img.shields.io/badge/python-2.6%2B%2C%203.3%2B-red.svg
   :target: https://pypi.python.org/pypi/python-starter
.. |PyPI| image:: https://img.shields.io/pypi/v/python-starter.svg
   :target: https://pypi.python.org/pypi/python-starter
