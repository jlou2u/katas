
# extract a slice from a list

def slice(i, k, l):
    return l[i:k]


def test_slice():

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    assert slice(3, 7, l) == ['d', 'e', 'f', 'g']

    assert slice(0, len(l), l) == l
    assert slice(0, 1, l) == ['a']
    assert slice(0, 2, l) == ['a', 'b']
    assert slice(0, 3, l) == ['a', 'b', 'c']
    assert slice(1, 3, l) == ['b', 'c']
    assert slice(2, 3, l) == ['c']
    assert slice(3, 3, l) == []
