from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
CYTHON_COMPILER_DIRECTIVES = {
    "language_level": 3,
}

CYTHON_EXTENSION_INCLUDES = ['.', np.get_include()]
CYTHON_EXTENSION_MODULES = [
    Extension('pycalphad.core.hyperplane', sources=['pycalphad/core/hyperplane.pyx']),
    Extension('pycalphad.core.eqsolver', sources=['pycalphad/core/eqsolver.pyx']),
    Extension('pycalphad.core.phase_rec', sources=['pycalphad/core/phase_rec.pyx']),
    Extension('pycalphad.core.composition_set', sources=['pycalphad/core/composition_set.pyx']),
    Extension('pycalphad.core.minimizer', sources=['pycalphad/core/minimizer.pyx']),
]
setup(
        ext_modules=cythonize(
        CYTHON_EXTENSION_MODULES,
        compiler_directives=CYTHON_COMPILER_DIRECTIVES,
    ),
      include_dirs=[np.get_include()]
)