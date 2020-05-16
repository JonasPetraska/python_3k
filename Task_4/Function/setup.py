from distutils.core import setup, Extension

module = Extension("IsPrimeModule", sources = ["IsPrime.c"])

setup(name="IsPrimeModule",
		ext_modules = [module])