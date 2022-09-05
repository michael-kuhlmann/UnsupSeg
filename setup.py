from distutils.core import setup
from setuptools import find_packages


setup(
    name='unsup_seg',
    version='0.0',
    description='Forked from https://github.com/felixkreuk/UnsupSeg',
    author='',
    author_email='',
    license='',
    packages=find_packages(),
    install_requires=[
        'dill',
        'boltons',
        'librosa',
        'torchaudio',
    ],
)
