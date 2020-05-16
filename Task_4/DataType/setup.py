from distutils.core import setup, Extension
from setuptools import setup, Extension

module = Extension("pointModule", sources = ["Point.c"])

setup(name="pointModule",
		ext_modules = [module])
		
		
# ~$ python setup.py install --user
# ~$ python
# >>> import pointModule
# >>> p=pointModule.Point(3,4)
# >>> p.move(10,15)
