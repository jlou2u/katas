
# generate a random permutation of the elemtns of a list
from random import shuffle


def random_permute(l):
    r = [_ for _ in l]
    shuffle(r)
    return r


def test_random_permute():

    l = ['a', 'b', 'c', 'd', 'e', 'f']
    r = random_permute(l)
    assert sorted(l) == sorted(r)

    # TODO: better ways to test?  maybe set random to known value and check
    # exact output?
