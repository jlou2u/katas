
# duplicate the elements of a list

def duplicate(l):
    result = []
    [result.extend([e, e]) for e in l]
    return result


def test_duplicate():

    l = ['a', 'b', 'c', 'c', 'd']
    assert duplicate(l) == ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd']

    assert duplicate([]) == []
    assert duplicate([None]) == [None, None]
    assert duplicate([1, None, 'a']) == [1, 1, None, None, 'a', 'a']
    assert duplicate([1, 1]) == [1, 1, 1, 1]
