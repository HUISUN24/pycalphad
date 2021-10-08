from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
CYTHON_COMPILER_DIRECTIVES = {
    "language_level": 3,
}

CYTHON_EXTENSION_INCLUDES = ['.', np.get_include()]
CYTHON_EXTENSION_MODULES = [
    Extension('pycalphad.core.minimizer', sources=['pycalphad/core/minimizer.pyx']),
]
setup(
        ext_modules=cythonize(
        CYTHON_EXTENSION_MODULES,
        compiler_directives=CYTHON_COMPILER_DIRECTIVES,
    ),
      include_dirs=[np.get_include()]
)