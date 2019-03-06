from setuptools import setup

from FIX import __version__ as v

def readme():
    with open('README.md', 'r') as f:
        return f.read()

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
    include_package_data=True,
    zip_safe=False,
)

