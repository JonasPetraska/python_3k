from distutils.core import setup, Extension
from setuptools import setup, Extension

module = Extension("primeModule", sources = ["IsPrime.c"])

setup(name="primeModule",
		ext_modules = [module])
	
	
# ~$ python setup.py install --user
# ~$ python
# >>> import primeModule
# >>> primeModule.isPrime(10)