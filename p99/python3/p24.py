
# lotto: draw N different random numbers from the set 1..M
from random import sample

def lotto(n, m):
    return sample(range(1, m+1), n)

def test_lotto():

    r = lotto(6, 49)
    assert len(r) == 6
    assert sorted(set(r)) == sorted(r)
    assert min(r) >= 1
    assert max(r) <= 49

    assert lotto(1, 1) == [1]
    r = lotto(1, 2)
    assert len(r) == 1
    assert r[0] == 1 or r[0] == 2
