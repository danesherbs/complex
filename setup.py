from distutils.core import setup
from os import path
from pip._internal.req import parse_requirements


here = path.abspath(path.dirname(__file__))
install_reqs = parse_requirements(here + '/requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='complex',
    version='1.0',
    url='https://github.com/danesherbs/complex',
    install_requires=reqs
)
