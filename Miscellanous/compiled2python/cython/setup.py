from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    name="Spatial Math Cython",
    # cythonize() translates the .pyx to .c and compiles it
    ext_modules=cythonize(
        "spatial_mean_cython.pyx", 
        compiler_directives={'language_level': "3"}
    ),
    # Ensure the C compiler can find the NumPy headers
    include_dirs=[np.get_include()]
)

