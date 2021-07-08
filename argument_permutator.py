from collections.abc import Generator
from itertools import product
from functools import reduce
import operator


class ArgumentPermutator(Generator):
    def __init__(self, **kwargs):
        self.keys = kwargs.keys()
        self.length = reduce(operator.mul, map(len, kwargs.values()))
        self.arguments = product(*kwargs.values())

    def send(self, ignored_args=None):
        try:
            return dict(zip(self.keys, next(self.arguments)))
        except StopIteration as si:
            raise si

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration

    def __len__(self):
        return self.length
