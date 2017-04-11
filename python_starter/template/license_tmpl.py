# -*- coding: utf-8 -*-
from python_starter.template.core import Template
from python_starter.template.licenses import mit, gplv2, gplv3, lgpl, mpl, apache


class LicenseTemplate(Template):
    def __init__(self,
                 name='{name}/LICENSE',
                 body='Copyright (c) {year} {author}'):
        Template.__init__(self, name=name, body=body)


# MIT License
mit_tmpl = LicenseTemplate(body=mit.__doc__)

# GPL License v2
gplv2_tmpl = LicenseTemplate(body=gplv2.__doc__)

# GPL License v3
gplv3_tmpl = LicenseTemplate(body=gplv3.__doc__)

# LGPL(v3)
lgpl_tmpl = LicenseTemplate(body=lgpl.__doc__)

# MPL (v2)
mpl_tmpl = LicenseTemplate(body=mpl.__doc__)

# Apache License
apache_tmpl = LicenseTemplate(body=apache.__doc__)

# No License
none_tmpl = LicenseTemplate()

candidate = {
    'MIT': {
        'template': mit_tmpl,
        'classifiers_text': 'License :: OSI Approved :: MIT License'
    },
    'GPLv2': {
        'template': gplv2_tmpl,
        'classifiers_text':
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    },
    'GPLv3': {
        'template': gplv3_tmpl,
        'classifiers_text':
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    },
    'LGPL': {
        'template': lgpl_tmpl,
        'classifiers_text': 'License :: OSI Approved ::'
        ' GNU Library or Lesser General Public License (LGPL)'
    },
    'MPL': {
        'template': mpl_tmpl,
        'classifiers_text':
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)'
    },
    'Apache': {
        'template': apache_tmpl,
        'classifiers_text':
        'License :: OSI Approved :: Apache Software License'
    },
    'None': {
        'template': none_tmpl,
        'classifiers_text': 'License :: Other/Proprietary License'
    }
}


def choose(name='MIT'):
    if name in candidate.keys():
        return candidate[name]
    else:
        return candidate['None']
