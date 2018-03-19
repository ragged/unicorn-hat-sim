from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='unicorn_hat_sim',
    version='1.0.0',
    description='A simple Unicorn Hat simulator',
    long_description=long_description,
    url='https://github.com/jayniz/unicorn-hat-sim',
    author='jayniz',
    author_email='jannis@gmail.com',
    py_modules=['unicorn_hat_sim.py'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['pygame'],
)