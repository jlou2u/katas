
# find the Kth element of a list (0 based indexing)
# allow negative indexing since python does

def nth(n, l):
    if len(l) <= abs(n):
        return None
    return l[n]

# TODO: implement using non standard library version of list because this
#       is really cheating

def test_nth():

    l = [1, 2, 3]
    assert nth(0, l) == 1
    assert nth(1, l) == 2
    assert nth(2, l) == 3
    assert nth(3, l) is None
    assert nth(-1, l) == 3


from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.lists(st.integers()))
def test_hyp(n, l):

    result = nth(n, l)

    if n >= 0:
        if len(l) > n:
            assert result == l[n]
        else:
            assert result is None
    else:
        if len(l) > abs(n) - 1:
            assert result == l[n]
        else:
            assert result is None
