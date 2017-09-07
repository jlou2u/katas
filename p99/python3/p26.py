
# generate the combinations of K distinct objects chosen
# from the N elements of a list
import itertools


def combinations(n, l):
    return [[x for x in y] for y in itertools.combinations(l, n)]


def test_combinations():

    assert combinations(1, ['a', 'b']) == [['a'], ['b']]
    assert combinations(1, ['a', 'b', 'c']) == [['a'], ['b'], ['c']]
    assert combinations(2, ['a', 'b', 'c']) == [
        ['a', 'b'],
        ['a', 'c'],
        ['b', 'c'],
    ]
    assert combinations(3, ['a', 'b', 'c']) == [['a', 'b', 'c']]

    r = combinations(3, range(12))
    assert len(r) == 220
