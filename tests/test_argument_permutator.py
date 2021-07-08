import pytest
from argument_permutator.argument_permutator import ArgumentPermutator


def test_simple_args():

    ap = ArgumentPermutator(a=[1, 2], b=[True, False])
    assert next(ap) == dict(a=1, b=True)
    assert next(ap) == dict(a=1, b=False)
    assert next(ap) == dict(a=2, b=True)
    assert next(ap) == dict(a=2, b=False)
    with pytest.raises(StopIteration):
        _ = next(ap)
