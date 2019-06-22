from setuptools import setup
from setuptools import find_packages

setup(name='dlgo',
      version='0.1',
      description='Deep Learning and the Game of Go',
      url='https://github.com/genekuo-org/dlgobot',
      install_requires=['tensorflow', 'keras', 'gomill', 'Flask>=0.10.1', 'Flask-Cors', 'future', 'h5py', 'six'],
      license='MIT',
      packages=find_packages(),
      zip_safe=False)