from argument_permutator import ArgumentPermutator

ap = ArgumentPermutator(a=[1, 2], b=[True, False])


def func(**kwargs):
    print(', '.join(f'{kw}={arg}' for kw, arg in kwargs.items()))


for argument_permutation in ap:
    func(**argument_permutation)
