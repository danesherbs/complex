from setuptools import setup, find_packages

setup(
    name='complex_trouillon',
    version='0.1',
    packages=find_packages(exclude=['datasets*, efe*']),
    description='A wrapper for Trouillon et al. (2016) original Github repo.',
    long_description=open('README.md').read(),
    install_requires=['downhill', 'scikit-learn'],
    url='https://github.com/danesherbs/complex',
    author='Dane S',
    author_email='danesherbs@gmail.com'
)
