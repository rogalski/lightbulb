# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='lightbulb',
    version='0.0.1dev',
    description='Smart home built on top of Intel Edison platform.',
    url='http://github.com/rogalski/lightbulb',
    author=u'Łukasz Rogalski',
    author_email='rogalski.91@gmail.com',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask'
    ],
    zip_safe=False
)
