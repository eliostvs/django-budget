#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup

except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()

setup(
    name='django-budjet',
    version='0.0.1',
    description="""Forked from django-budget using Twitter Bootstrap 3""",
    long_description=readme,
    author='Elio Esteves Duarte',
    author_email='elio.esteves.duarte@gmail.com',
    url='https://github.com/eliostvs/django-budget',
    packages=[
        'django-budget',
    ],
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='django-budget',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
