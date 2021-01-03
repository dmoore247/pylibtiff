#!/usr/bin/env python

CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
License :: OSI Approved
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Scientific/Engineering
Topic :: Software Development
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

ISRELEASED = False

from setuptools import setup, find_packages

setup(
    name='pylibtiff',
    author='Pearu Peterson',
    author_email='pearu.peterson@gmail.com',
    version='0.4.4',
    url='https://github.com/pearu/pylibtiff',
    license='https://github.com/pearu/pylibtiff/blob/master/LICENSE',
    python_requires='>=2.7',
    install_requires=['numpy'],
    platforms=["All"],
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    description='PyLibTiff: a Python tiff library.',
    long_description='''\
	PyLibTiff? is a Python package that provides the following modules:
	libtiff - a wrapper of C libtiff library using ctypes.
	tiff - a numpy.memmap view of tiff files.
    ''',
    packages=find_packages(),
)
