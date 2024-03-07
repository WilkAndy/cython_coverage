from distutils.core import setup, Extension
from Cython.Build import cythonize

compiler_directives = {}
define_macros = []

compiler_directives['profile'] = True
compiler_directives['linetrace'] = True
compiler_directives['language_level'] = 3
define_macros.append(('CYTHON_TRACE', '1'))

setup(ext_modules = cythonize(Extension(
       "cyApple",
       sources=["cyApple.pyx", "apple.cpp"],
       define_macros=define_macros,
       language="c++",
  ), compiler_directives=compiler_directives))
