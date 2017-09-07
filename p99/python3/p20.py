
# remove the Kth element from a list

def remove_at(n, l):
    if len(l) == 0:
        return l
    if n < 0:
        l = l[::-1]
        n = -1*n-1
        r = l[0:n] + l[n+1:]
        return [r[::-1], l[n]]
    return [l[0:n] + l[n+1:], l[n]]


def test_remove_at():

    assert remove_at(1, ['a', 'b', 'c', 'd']) == [['a', 'c', 'd'], 'b']
    assert remove_at(0, ['a', 'b', 'c', 'd']) == [['b', 'c', 'd'], 'a']
    assert remove_at(-1, ['a', 'b', 'c', 'd']) == [['a', 'b', 'c'], 'd']
    assert remove_at(-2, ['a', 'b', 'c', 'd']) == [['a', 'b', 'd'], 'c']
    assert remove_at(-3, ['a', 'b', 'c', 'd']) == [['a', 'c', 'd'], 'b']
    assert remove_at(-4, ['a', 'b', 'c', 'd']) == [['b', 'c', 'd'], 'a']

    assert remove_at(0, []) == []
    assert remove_at(1, []) == []
    assert remove_at(0, [None]) == [[], None]
