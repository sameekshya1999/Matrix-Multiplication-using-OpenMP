from setuptools import setup, Extension

module = Extension('matrix',
                   sources=['matrix_module.c'],
                   extra_compile_args=['-fopenmp'],
                   extra_link_args=['-fopenmp'])

setup(
    name='matrix',
    version='1.0',
    ext_modules=[module]
)