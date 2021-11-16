import pytest
from argument_permutator import ArgumentPermutator


def test_empty_argument_permutator():

    ap = ArgumentPermutator()
    assert len(ap) == 0
    with pytest.raises(StopIteration):
        _ = next(ap)


def test_fixed_kwargs():

    ap = ArgumentPermutator(dict(fixed_kwarg1="DEBUG", fixed_kwargs2=11))
    assert len(ap) == 0
    with pytest.raises(StopIteration):
        _ = next(ap)


def test_variable_kwargs():

    ap = ArgumentPermutator(a=[1, 2], b=[True, False])
    assert next(ap) == dict(a=1, b=True)
    assert next(ap) == dict(a=1, b=False)
    assert next(ap) == dict(a=2, b=True)
    assert next(ap) == dict(a=2, b=False)
    with pytest.raises(StopIteration):
        _ = next(ap)


def test_fixed_and_variable_kwargs():

    ap = ArgumentPermutator(dict(fixed_kwarg1="DEBUG", fixed_kwargs2=11), var_kwargs=['a', 'b', 'c'])
    assert len(ap) == 3
    assert next(ap) == dict(fixed_kwarg1="DEBUG", fixed_kwargs2=11, var_kwargs='a')
    assert len(ap) == 2
    assert next(ap) == dict(fixed_kwarg1="DEBUG", fixed_kwargs2=11, var_kwargs='b')
    assert len(ap) == 1
    assert next(ap) == dict(fixed_kwarg1="DEBUG", fixed_kwargs2=11, var_kwargs='c')
    assert len(ap) == 0
    with pytest.raises(StopIteration):
        _ = next(ap)


def test_len_argument_permutator():

    ap = ArgumentPermutator(a=[1, 2], b=[True, False])
    assert len(ap) == 4


def test_empty_input_variable_kwargs():

    ap = ArgumentPermutator(a=[])
    assert len(ap) == 0
    with pytest.raises(StopIteration):
        _ = next(ap)
