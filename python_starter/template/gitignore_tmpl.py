# -*- coding: utf-8 -*-
from python_starter.template.core import Template

gitignore_body = '''__pycache__/
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
'''

gitignore_tmpl = Template(name='{name}/.gitignore', body=gitignore_body)
