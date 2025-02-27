#!/usr/bin/env python3
# encoding: utf-8
#
# This file is part of ckanext-doi
# Created by the Natural History Museum in London, UK

from setuptools import find_packages, setup

__version__ = '3.0.7'

with open('README.md', 'r') as f:
    __long_description__ = f.read()

setup(
    name='ckanext-doi',
    version=__version__,
    description='A CKAN extension for assigning a digital object identifier (DOI) to datasets, '
                'using the DataCite DOI service.',
    long_description=__long_description__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='CKAN data doi',
    author='Natural History Museum',
    author_email='data@nhm.ac.uk',
    url='https://github.com/flaviofrancisco/ckanext-doi',
    license='GNU GPLv3',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.doi'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'datacite==1.1.2',
        'xmltodict==0.12.0',
        'jsonschema==3.0.0',
    ],
    entry_points= \
        '''
        [ckan.plugins]
            doi=ckanext.doi.plugin:DOIPlugin
        ''',
)
