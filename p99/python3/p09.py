
# pack consecutive duplicates of list elements into sublists

def pack(l):
    if len(l) == 0:
        return l
    last = l[0]
    result = [[last]]
    for e in l[1:]:
        if e == last:
            result[-1].append(e)
        else:
            result.append([e])
        last = e
    return result


def test_pack():

    l = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    expected = [
        ['a', 'a', 'a', 'a'],
        ['b'],
        ['c', 'c'],
        ['a', 'a'],
        ['d'],
        ['e', 'e', 'e', 'e']
    ]
    assert pack(l) == expected

    l = ['a', 'a', 'a']
    assert pack(l) == [['a', 'a', 'a']]

    l = []
    assert pack(l) == []

    l = [1, 'a', 2, 2]
    assert pack(l) == [[1], ['a'], [2, 2]]

    assert pack([1]) == [[1]]

