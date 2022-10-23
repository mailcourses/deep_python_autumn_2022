from setuptools import setup, Extension

setup(
    name = 'cutils',
    version = '1.0',
    description = 'Example of C extension',
    author = 'Anton Kukhtichev',

    ext_modules = [
        Extension('cutils', ['cutils.c'])
    ]
)
