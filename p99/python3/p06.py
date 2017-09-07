
# find out whether a list is a palindrome

def is_palindrome(l):

    length = len(l)
    for i in range(length // 2):
        if l[i] != l[-1*(i+1)]:
            return False
    return True


def test_palindrome():

    palindromes = [
        [],
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 2, 3, 2, 1],
        [None],
        [None, None],
        [None, None, None],
        [None, 1, None],
        [1, None, 1],
        [-1, -1, -1],
        [[], []]
    ]

    for l in palindromes:
        assert is_palindrome(l)

    not_palindromes = [
        [1, 2],
        [None, 1, 1],
        [0, 0, 1],
        [0, 0, 0, None],
    ]

    for l in not_palindromes:
        assert not is_palindrome(l)


from hypothesis import given, example
import hypothesis.strategies as st


@given(st.lists(st.integers()))
@example([1, 2, 3])
@example([1, 1, 1])
@example([])
@example([-1, 2, -1])
@example([None])
@example([None, None])
@example([None, None, None])
def test_hyp(l):

    result = is_palindrome(l)

    offset = len(l) // 2
    expected = l[0:offset] == list(reversed(l))[0:offset]

    assert expected == result
