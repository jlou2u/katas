
# extract a given number of randomly selected elements from a list
from random import sample

def random_select(n, l):
    return sample(l, n)


def test_random_select():

    l = ['a', 'b', 'c', 'd', 'f', 'g', 'h']
    r = random_select(3, l)
    assert len(r) == 3
    assert r[0] in l
    assert r[1] in l
    assert r[2] in l

    assert random_select(0, []) == []
    assert random_select(1, ['a']) == ['a']

    r = random_select(1, ['a', 'b'])
    assert r == ['a'] or r == ['b']
