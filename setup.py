#!/usr/bin/env python
# coding: utf-8
"""
   File Name: setup.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:24:31 2014 CST
"""
DESCRIPTION = """
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='bitmap',
      version='0.0.3',
      author='WAN Ji',
      author_email='wanji@live.com',
      package_dir={'bitmap': 'src'},
      packages=['bitmap'],
      url='http://pypi.python.org/pypi/bitmap/',
      # license='LICENSE.txt',
      description='.',
      long_description=open('README.md').read(),
      install_requires=[
          # "numpy      >= 1.7.0",
          # "leveldb    >= 0.192",
      ],
      )
