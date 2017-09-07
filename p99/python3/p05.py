
# reverse a list

def rev(l):
    return l[::-1]


from hypothesis import given
import hypothesis.strategies as st


@given(st.lists(st.integers()))
def test_hyp(l):
    assert list(reversed(l)) == rev(l)
