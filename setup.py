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
      version='0.0.7',
      author='WAN Ji',
      author_email='wanji@live.com',
      package_dir={'bitmap': 'src'},
      packages=['bitmap'],
      url='https://github.com/wanji/bitmap',
      # license='LICENSE.txt',
      description='.',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      install_requires=[
          'future',
      ],
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7',
      ],
      )
