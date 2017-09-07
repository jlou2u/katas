
# modified run length encoding of a list
# if no duplicates for element, just copy element instead of [N, e]
from p09 import pack

def encode(l):
    def _enc(x):
        return [len(x), x[0]] if len(x) > 1 else x[0]
    return [_enc(sl) for sl in pack(l)]


def test_encode():

    l = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    expected = [[4, 'a'], 'b', [2, 'c'], [2, 'a'], 'd', [4, 'e']]
    assert encode(l) == expected

    assert encode([]) == []
    assert encode([1, 1, 1]) == [[3, 1]]
    assert encode(['x']) == ['x']
    assert encode([None]) == [None]
    assert encode([None, None]) == [[2, None]]
    assert encode([[], [], []]) == [[3, []]]
    assert encode([[], 'a', 'a']) == [[], [2, 'a']]
