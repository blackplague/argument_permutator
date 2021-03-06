# Argument Permutator

## Installation

The Argument Permutator can be installed directly from git using

```sh
#> python -m pip install git+https://github.com/blackplague/argument_permutator.git
```

or from pypi using ...

## Usage

The ArgumentPermutator can be used to run automated test or benchmarks of functions requiring
keyword arguments. As an example see *demo.py* below.

demo.py:

```python
from argument_permutator import ArgumentPermutator

ap = ArgumentPermutator(a=[1, 2], b=[True, False])


def print_args_func(a: int, b: bool):
    if a == 1:
        if b:
            print('a is 1 and b is True')
        elif b == False:
            print('a is 1 and b is _NOT_ True')
        else:
            print('We should hopefully never hit this situation...')
    elif a == 2:
        if b:
            print('a is two and b is True')
        elif b == False:
            print('a is still two and b is false')
        else:
            print('We should also never reach this...')
    else:
        print('This is also very wrong...')


print(f'There is a total of {len(ap)} different argument permutations.')

for argument_permutation in ap:
    print_args_func(**argument_permutation)

```

The *demo.py* will output the following:

```text
There is a total of 4 different argument permutations.
a is 1 and b is True
a is 1 and b is _NOT_ True
a is two and b is True
a is still two and b is false
```

## Release History

* 0.1.5
  * Still in pre-release

## Meta

Michael Andersen - michael10andersen+argperm -[at]- gmail.com - [Github](https://github.com/blackplague/)

Distributed under the LGPL3 license. See ``LICENSE`` for more information.
