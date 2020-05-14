try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'xontrib-enhancd',
    version = '0.1.0',
    author = 'sun-yryr',
    author_email = 'taittide@gmail.com',
    description = 'b4b4r07/enhancd for xonsh',
    long_description = open('README.md').read(),
    url = 'https://github.com/sun-yryr/xontrib-enhancd',
    license = 'MIT',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    packages = ['xontrib'],
    package_dir = {'xontrib': 'xontrib'},
    package_data = {'xontrib': ['./**/*.py']},
    platforms = 'any',
)
