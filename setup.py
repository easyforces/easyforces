# coding=utf-8
# Author: LucasD11
#
"""
Package Configure

This file will define anything required for a python package.

To upload the package, using::
   python setup.py sdist bdist_wheel
   twine upload dist/*
"""

from setuptools import setup


description="Command line tools for practicing and competiting on Code Forces."

long_description=(
    "Easy Forces Command Line Tool helper command for Code Forces. It will "
    "help you parsing problems, running patch tests and submiting problems on "
    "Code Forces."
)


setup(
    name='easyforces',
    version='0.1.0',
    description=description,
    long_description=long_description,
    url='https://www.easyforces.com',
    author='EasyForces Team',
    author_email='yuanzhendai@gmail.com',
    license='MIT',
    packages=['easyforces'],
    zip_safe=False,
    long_description_content_type='text/x-rst'
)
