"""
Allows installation via pip, e.g. by navigating to this directory with the command prompt, and using 'pip install .'
"""

import sys
from setuptools import setup, find_packages

setup(
    name='torch',
    version='0.1a',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scipy', 'ambiance', 'thermo==0.1.40', 'gas_dynamics'],
    description='Python version of NASA aerodynamic heating program NQLDW019',
)
