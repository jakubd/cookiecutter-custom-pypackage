import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.package_version }}",
    url="https://github.com/{{ cookiecutter.author_github_user }}/{{ cookiecutter.package_name }}",
    license='BSD-3-Clause',

    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",

    description="{{ cookiecutter.package_description }}",
    long_description=read("README.md"),

    packages=find_packages(exclude=('tests',)),

    install_requires=requirements,

    tests_require=[
        "pytest"
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
