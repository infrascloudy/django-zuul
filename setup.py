import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()

setup(
    name='django-zuul',
    version='1.0.1',
    keywords = ('django', 'apigateway', 'dataproxy'),
    description = 'apigateway powered by django',
    install_requires=['django==2.1.7',
                      'requests',
                      'djangorestframework',
                      'psycopg2-binary'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    long_description=read('README.md'),
    url='https://github.com/infrascloudy/django-zuul'
)
