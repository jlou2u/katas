
# drop every Nth element from a list

def drop(n, l):
    if n <= 0:
        return []
    return [e for i, e in enumerate(l) if (i+1) % n != 0]


def test_drop():

    l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    assert drop(3, l) == ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k']

    assert drop(0, ['a', 'b', 'c']) == []
    assert drop(1, ['a', 'b', 'c']) == []
    assert drop(2, ['a', 'b', 'c']) == ['a', 'c']
    assert drop(3, ['a', 'b', 'c']) == ['a', 'b']
    assert drop(4, ['a', 'b', 'c']) == ['a', 'b', 'c']
