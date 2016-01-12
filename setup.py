#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


required = [
    "Django==1.8.8",
    "gevent==1.0.2",
    "gunicorn==19.4.5",
    "psycogreen==1.0",
    "psycopg2==2.6.1",
]


setup(
    name = "async-django-gevent-demo",
    version = "0.0",
    author = "Sam Madhani",
    author_email = "shemzzz@gmail.com",
    description = ("A scaffold app (sort of) for Django, Gunicorn, Gevent",
                   "Psycopg2. Includes a demo of realized concurrency."),
    license = "MIT",
    keywords = "Django Gunicorn Gevent Psycopg2 Async Concurrent",
    url = "https://github.com/smahs/async-django-gevent-demo",
    packages=[''],
#    long_description=read('README.md'),
    install_requires=required,
    classifiers=[
        "Development Status :: 0 - Final",
        "Intended Audience :: Developers",
        "Topic :: Web",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
)
