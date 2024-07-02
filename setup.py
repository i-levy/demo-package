import numpy as np
from setuptools import setup

setup(
    name='get_num',
    version='0.1',
    url='https://github.com/i-levy/demo-package',
    author='Isaac Levy',
    author_email='isaac.levy21@gmail.com',
    description='Generate a random integer',
    packages=['gen_num'],    
    install_requires=['numpy >= 1.11.1'],
)