"""A argument permutation generator for automated benchmarking and testing.

.. module:: argument_permutator.py
    :platform: GNU/Linux
    :synopsis: Creates a generator for generating permutation of keyword arguments based on
               inputs, that is returned as a dictionary that can be used as arguments for
               a function. As an example see demo.py.

.. moduleauthor:: Michael Andersen <michael10andersen+argperm@gmail.com>
"""
from collections.abc import Generator
from functools import reduce
from itertools import product
from operator import mul
from typing import Dict


class ArgumentPermutator(Generator):
    def __init__(self, fixed_kwargs: Dict=None, **kwargs):
        self.fixed_kwargs = fixed_kwargs
        self.arguments = product(*kwargs.values()) if kwargs.values() else None
        self.keys = kwargs.keys()
        self.length = reduce(mul, map(len, kwargs.values())) if kwargs.values() else 0

    def send(self, ignored_args=None):
        if self.arguments is None:
            raise StopIteration
        try:
            if self.fixed_kwargs:
                kwargs = {**dict(self.fixed_kwargs), **dict(zip(self.keys, next(self.arguments)))}
            else:
                kwargs = dict(zip(self.keys, next(self.arguments)))
            self.length -= 1
            return kwargs
        except StopIteration as si:
            raise si

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration

    def __len__(self):
        return self.length
