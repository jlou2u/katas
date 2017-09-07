
# find the last but one element of a list

def penultimate(l):
    if len(l) < 2:
        return None
    return l[-2]


from hypothesis import given
import hypothesis.strategies as st


def test_penultimate():

    l = [1, 2, 3]
    assert penultimate(l) == 2

    l = [1]
    assert penultimate(l) is None

    l = [1, 'a', 9]
    assert penultimate(l) == 'a'


@given(st.lists(elements=st.integers()))
def test_hyp(l):
    result = penultimate(l)
    if len(l) < 2:
        assert result is None
    else:
        assert result == l[::-1][1]
