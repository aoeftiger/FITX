from setuptools import setup

from FITX import __version__ as v

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='FITX',
    version=v,
    description='Fit my InsTability eXponential',
    long_description='A library to isolate and fit exponential rise times in unstable systems with saturation.',
    url='https://github.com/aoeftiger/FITX',
    author='Adrian Oeftiger',
    author_email='adrian@oeftiger.net',
    license='MIT',
    packages=['FITX'],
    install_requires=['numpy'],
    include_package_data=True,
    zip_safe=False,
)

