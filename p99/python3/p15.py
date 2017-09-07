
# duplicate the elements of a list a given number of times

def duplicate_n(n, l):
    result = []
    [result.extend([e for _ in range(n)]) for e in l]
    return result


def test_duplicate_n():

    l = ['a', 'b', 'c', 'c', 'd']
    expected = [
        'a', 'a', 'a',
        'b', 'b', 'b',
        'c', 'c', 'c',
        'c', 'c', 'c',
        'd', 'd', 'd'
    ]
    assert duplicate_n(3, l) == expected

    assert duplicate_n(0, l) == []
    assert duplicate_n(1, l) == l
    assert duplicate_n(-1, l) == []
