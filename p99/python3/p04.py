
# find the number of elements of a list

def length(l):
    return len(l)


from hypothesis import given
import hypothesis.strategies as st


@given(st.lists(st.integers()))
def test_hyp(l):
    assert len(l) == length(l)
