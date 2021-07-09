# Argument Permutator

## Installation

The Argument Permutator can be installed directly from git using

```sh
#> python -m pip install git+https://github.com/blackplague/argument_permutator.git
```

or from pypi using ...

## Usage

This ...

demo.py:

```python
from argument_permutator import ArgumentPermutator

ap = ArgumentPermutator(a=[1, 2], b=[True, False])


def print_args_func(**kwargs):
    print(', '.join(f'{kw}={arg}' for kw, arg in kwargs.items()))


print(f'There is a total of {len(ap)} different argument permutations.')

for argument_permutation in ap:
    print_args_func(**argument_permutation)

```

## TODO

Add a license

And this concludes the README.md
