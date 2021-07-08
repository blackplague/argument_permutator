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

def func(**kwargs):
    for kw, arg in kwarg.items():
        print(f'{kw}={arg}')

for argument_permutation in ap:
    func(**argument_permutation)
```

## TODO

Add a license

And this concludes the README.md
