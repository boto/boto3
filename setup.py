#!/usr/bin/env python

"""
distutils/setuptools install script.
"""

import os
import re

from setuptools import find_packages, setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'botocore>=1.35.34,<1.36.0',
    'jmespath>=0.7.1,<2.0.0',
    's3transfer>=0.10.0,<0.11.0',
]


def get_version():
    init = open(os.path.join(ROOT, 'boto3', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='boto3',
    version=get_version(),
    description='The AWS SDK for Python',
    long_description=open('README.rst').read(),
    author='Amazon Web Services',
    url='https://github.com/boto/boto3',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={'boto3': ['data/aws/resources/*.json', 'examples/*.rst']},
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    python_requires=">= 3.8",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    project_urls={
        'Documentation': 'https://boto3.amazonaws.com/v1/documentation/api/latest/index.html',
        'Source': 'https://github.com/boto/boto3',
    },
)
