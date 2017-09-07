
# run length encoding of a list
from p09 import pack

def encode(l):
    return [[len(sl), sl[0]] for sl in pack(l)]


def test_encode():

    l = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    expected = [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
    assert encode(l) == expected

    assert encode([]) == []
    assert encode([1, 1, 1]) == [[3, 1]]
    assert encode(['x']) == [[1, 'x']]
    assert encode([None]) == [[1, None]]
    assert encode([None, None]) == [[2, None]]
    assert encode([[], [], []]) == [[3, []]]
