
# eliminate consecutive duplicates of list elements
# if a list contains repeated elements they should be replaced with a single
# copy of the element.  the order of the elements should not be changed.

def compress(l):
    if len(l) == 0:
        return l
    return [l[i-1] for i in range(1, len(l)) if l[i] != l[i-1]] + [l[-1]]


def test_compress():

    l = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    assert compress(l) == ['a', 'b', 'c', 'a', 'd', 'e']

    l = []
    assert compress(l) == []

    l = [1, 1]
    assert compress(l) == [1]

    l = [None, None]
    assert compress(l) == [None]

    l = ['a', 'a', 'a', 2, 'b', 'b', None, None, 1, None, 1]
    assert compress(l) == ['a', 2, 'b', None, 1, None, 1]

    l = ['a', 'a', {}]
    assert compress(l) == ['a', {}]
