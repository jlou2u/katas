
# decode a run length encoded list

def decode(l):
    result = []
    [result.extend([e for _ in range(n)]) for n, e in l]
    return result


def test_decode():

    l = [[4, 'a'], [1, 'b'], [2, 'c'], [2, 'a'], [1, 'd'], [4, 'e']]
    expected = [
        'a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e'
    ]
    assert decode(l) == expected

    assert decode([]) == []
    assert decode([[1, 100]]) == [100]
    assert decode([[5, 100]]) == [100, 100, 100, 100, 100]
    assert decode([[0, 100]]) == []
    assert decode([[2, None], [1, 'a'], [1, None]]) == [None, None, 'a', None]

