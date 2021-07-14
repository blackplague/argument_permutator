"""A argument permutation generator for automated benchmarking and testing.

.. module:: argument_permutator.py
    :platform: GNU/Linux
    :synopsis: Creates a generator for generating permutation of keyword arguments based on
               inputs, that is returned as a dictionary that can be used as arguments for
               a function. As an example see demo.py.

.. moduleauthor:: Michael Andersen <gosuckadeadcow+github@gmail.com>
"""
from collections.abc import Generator
from functools import reduce
from itertools import product
from operator import mul


class ArgumentPermutator(Generator):
    def __init__(self, **kwargs):
        self.arguments = product(*kwargs.values())
        self.keys = kwargs.keys()
        self.length = reduce(mul, map(len, kwargs.values()))

    def send(self, ignored_args=None):
        try:
            return dict(zip(self.keys, next(self.arguments)))
        except StopIteration as si:
            raise si

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration

    def __len__(self):
        return self.length
