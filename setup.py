from setuptools import setup

import FIX.__version__ as v

setup(
   name='FIX',
   version=v,
   description='Fit my Instability eXponential',
   long_description='A library to isolate and fit exponential rise times in unstable systems with saturation.',
   url='https://github.com/aoeftiger/FIX',
   author='Adrian Oeftiger',
   author_email='adrian@oeftiger.net',
   license='MIT',
   packages=['FIX'],
   install_requires=['numpy'],
   zip_safe=False,
)

