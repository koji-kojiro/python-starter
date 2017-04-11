# -*- coding: utf-8 -*-
import os


class Template(object):
    def __init__(self, name, body):
        self.filename = os.path.basename(name)
        self.path = os.path.dirname(name)
        self.body = body
        self.isdir = not self.filename

    def make(self, root, **params):
        path = os.path.join(root, self.path.format(**params))
        filename = self.filename.format(**params)
        body = self.body.format(**params)
        Template.mktree(path)
        if not self.isdir:
            with open(os.path.join(path, filename), 'w') as fp:
                fp.write(body)

    @staticmethod
    def mktree(path):
        path_list = path.split('/')
        for i, _ in enumerate(path_list):
            _path = os.path.join(*path_list[:i + 1])
            if not os.path.exists(_path):
                os.mkdir(_path)
