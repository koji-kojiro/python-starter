# python-starter -- 'module-starter' for Python
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)  


## Requirements
**python-starter** does not require any other packages or modules. Please confirm whether the following condition is satisfied.  
- python >= (2.6, 3.3)


## Installation
Use `pip` or `easy_install`.  
```
$ pip install python-starter
```

## Usage
```
$ python-starter --help
usage: pyton [-h] [--author [author]] [--email [email]] [--license [license]]
             name

positional arguments:
  name                 project name

optional arguments:
  -h, --help           show this help message and exit
  --author [author]    author name (default: git user.name)
  --email [email]      author email (default: git user.email)
  --license [license]  license (default: MIT)
                       ['None', 'LGPL', 'MPL', 'GPLv2', 'GPLv3', 'Apache', 'MIT']
``` 
**python-starter** is designed to work with Git to minimize user input. If Git is installed on your PC, author's name and e-mail address will be automaticaly filled from git config. What you need to do is just excuting the following simple command in your terminal.  
```
$ python-starter {name}
```
Then, your project skeleton will be created with the following structure.  
```
{name}
├── .gitignore
├── LICENSE
├── README.rst
├── setup.py
└── {name}
    └── __init__.py

1 directory, 5 files
```

## Example
```
$ git config --get user.name
foo
$ git config --get user.email
foo@bar.com
$ python-starter example
```

### [example/setup.py](example/setup.py)
```python
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
```

### [example/LICENSE](example/LICENSE)
```
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
```

### [example/README.rst](example/README.rst)
```reST
example
--------
```

### [example/.gitignore](example/.gitignore)
```
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
```


## License
Distributed under MIT License.  

## Author
[Kojiro TANI](https://github.com/koji-kojiro "koji-kojiro") (kojiro0531@gmail.com)
