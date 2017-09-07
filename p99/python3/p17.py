
# split a list into two parts

def split(n, l):
    return [l[0:n], l[n:]]


def test_split():

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    expected = [['a', 'b', 'c'], ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k']]
    assert split(3, l) == expected

    assert split(3, []) == [[], []]
    assert split(0, []) == [[], []]
    assert split(1, ['a']) == [['a'], []]
    assert split(0, ['a']) == [[], ['a']]
    assert split(0, ['a', 'b', 'c']) == [[], ['a', 'b', 'c']]
    assert split(10, ['a', 'b', 'c']) == [['a', 'b', 'c'], []]
