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

## License

The choice of license is based on the fact that the library is as simple as it is. It would not
make sense to choose another one.

See the file **LICENSE.md**

## TODO

And this concludes the README.md
