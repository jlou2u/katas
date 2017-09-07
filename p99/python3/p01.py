
# find the last element of a list
# use python's built in list indexing with a special case for an empty list
# note: I believe cpython keeps track of a list's length for quick lookup so
#       len() does not require a traversal, only field lookup, but I should
#       find where that's spelled out or write a test to prove it...
def last(l):
    if len(l) == 0:
        return None
    return l[-1]


from hypothesis import given
import hypothesis.strategies as st


def test_last():

    l = [1, 2, 3]
    assert last(l) == 3

    l = [1, 'a', 'b']
    assert last(l) == 'b'

    l = []
    assert last(l) == None


@given(st.lists(elements=st.integers()))
def test_hyp(l):
    result = last(l)
    if len(l) == 0:
        assert result is None
    else:
        assert result == l[-1]
