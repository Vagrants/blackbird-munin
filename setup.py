#!/usr/bin/env python
# -*- codig: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='blackbird-munin',
    version='0.1.0',
    description=(
        'blackbird pplugin for munin-node'
    ),
    author='ARASHI, Jumpei',
    author_email='jumpei.arashi@arashike.com',
    url='https://github.com/Vagrants/blackbird-munin',
)
