from setuptools import setup, Extension

from Cython.Build import cythonize

ext_modules = [Extension("cymath.cymath", sources=["cymath/cymath.pyx", "cymath/fab.c"]),
               Extension("cymath.test", sources=["cymath/test.pyx"])]

setup(
    name="cymath",
    ext_modules=cythonize(ext_modules)
)
import aioaria2