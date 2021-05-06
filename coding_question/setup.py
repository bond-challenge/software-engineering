#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='custom-interface',
    version='0.0.1',
    author='Rafael',
    author_email='contact@rafagomes.com',
    maintainer='Rafael',
    maintainer_email='contact@rafagomes.com',
    license='Apache Software License 2.0',
    url='https://github.com/bond-challenge/software-engineering',
    description='Sample of an interface for a data structure',
    long_description=read('README.rst'),
    py_modules=['interface'],
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
)
