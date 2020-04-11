from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='amaryllis',
    packages=['amaryllis', 'amaryllis.models', 'amaryllis.util', 'amaryllis.survival_rate'], 
    version='1.0.10',
    license='MIT', 
    install_requires=['numpy'], 
    author='yk-amary-20', 
    author_email='y.k.83600260@gmail.com', 
    description='To calculate insurance value', 
    long_description=long_description, 
    long_description_content_type='text/markdown',  
    keywords='amaryllis',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ], 
)