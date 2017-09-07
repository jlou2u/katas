
# rotate a list N places to the left

def rotate(n, l):
    return l[n:] + l[0:n]


def test_rotate():

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    expected =         ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'a', 'b', 'c']
    assert rotate(3,l) == expected

    expected = ['j', 'k', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    assert rotate(-2, l) == expected

    assert rotate(0, l) == l
    assert rotate(0, ['a']) == ['a']
    assert rotate(1, ['a']) == ['a']
    assert rotate(-1, ['a']) == ['a']
    assert rotate(100, ['a']) == ['a']

    assert rotate(0, ['a', 'b']) == ['a', 'b']
    assert rotate(1, ['a', 'b']) == ['b', 'a']
    assert rotate(2, ['a', 'b']) == ['a', 'b']

    # not sure how it should work when n > len(list), but this is by default
    assert rotate(3, ['a', 'b']) == ['a', 'b']
