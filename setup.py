"""Compile the Cython module in file `dep/cython_util.pyx`.

Compile with:
    $ python setup.py build_ext --inplace

"""

from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("dep/cython_util.pyx"),
	include_dirs = [numpy.get_include()]
)

