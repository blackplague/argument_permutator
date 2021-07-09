from argument_permutator import ArgumentPermutator

ap = ArgumentPermutator(a=[1, 2], b=[True, False])


def print_args_func(**kwargs):
    print(', '.join(f'{kw}={arg}' for kw, arg in kwargs.items()))


print(f'There is a total of {len(ap)} different argument permutations.')

for argument_permutation in ap:
    print_args_func(**argument_permutation)
