from setuptools import setup, find_packages

setup(
    name='django-zuul',
    version='1.0.0',
    keywords = ('django', 'apigateway', 'dataproxy'),
    description = 'apigateway powered by django',
    install_requires=['django==2.1.7',
                      'requests',
                      'djangorestframework',
                      'psycopg2-binary'],
    packages=find_packages(exclude=['tests']),
    include_package_data=True
)
