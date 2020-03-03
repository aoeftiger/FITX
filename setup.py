from setuptools import setup

from FITX import __version__ as v

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='FITX',
    version=v,
    description='Fit my InsTability eXponential',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/aoeftiger/FITX',
    author='Adrian Oeftiger',
    author_email='adrian@oeftiger.net',
    license='MIT',
    packages=['FITX'],
    install_requires=['numpy'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.6",
)
