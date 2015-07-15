#!/usr/bin/env python
from distutils.core import setup

setup(name='jsoncat',
      description='Pretty-print streams of json objects',
      version='0.1',
      author='Alex Flint',
      author_email='alex.flint@gmail.com',
      url='https://github.com/alexflint/jsoncat',
      packages=['jsoncat'],
      package_dir={'jsoncat': '.'},
      scripts=['cmds/jsoncat']
      )
