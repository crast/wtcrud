import sys

extra = {}

try:
    from setuptools import setup
    has_setuptools = True
    extra['test_suite'] = 'tests.runtests'
except ImportError:
    from distutils.core import setup
    has_setuptools = False

if sys.version_info >= (3, ):
    if not has_setuptools:
        raise Exception('Python3 support in WTForms requires distribute.')

setup(
    name='WTCrud',
    version='0.1dev',
    url='http://github.com/crast/wtcrud',
    license='BSD',
    author='James Crasta',
    author_email='wtcrud@jamescrasta.com',
    description='CRUD forms for WTForms using Flask, Jinja2, SQLAlchemy',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'wtcrud',
    ],
    package_data={
    },
    **extra
)
