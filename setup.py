from setuptools import setup, find_packages

desc = '''An argument permutator generator for generating argument permutations for running automated tests
and or benchmarks'''

setup(
    name='ArgumentPermutator',
    version='0.1',
    description=desc,
    author='Michael Andersen',
    author_email='gosuckadeadcow+pypi@gmail.com',
    packages=find_packages(exclude=['tests'])
)
