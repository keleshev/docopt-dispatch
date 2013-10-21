import re
import os

from setuptools import setup

import docopt_dispatch as module


author, email = re.match('(.*?)<(.*?)>', module.__author__).groups()
description = module.__doc__.partition('.')[0]
classifiers = [
    'Development Status :: 3 - Alpha',
    'Topic :: Utilities',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
]
requires = ['docopt']


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name=module.__name__.replace('_', '-'),
    version=module.__version__,
    author=author,
    author_email=email,
    description=description,
    license=module.__license__,
    keywords=module.__keywords__,
    url=module.__url__,
    py_modules=[module.__name__],
    long_description=read('README.rst'),
    classifiers=classifiers,
    install_requires=requires,
)
