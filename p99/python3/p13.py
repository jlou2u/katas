
# run length encoding of a list (direct solution)

def encode_direct(l):
    result = []
    cnt = 0
    for i in range(len(l)):
        cnt = cnt + 1
        if i < len(l) - 1 and l[i] != l[i+1]:
            result.append([cnt, l[i]])
            cnt = 0
    if cnt > 0:
        result.append([cnt, l[-1]])
    return result


def test_encode_direct():

    l = ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
    expected = [[4,'a'], [1,'b'], [2,'c'], [2,'a'], [1,'d'], [4,'e']]
    assert encode_direct(l) == expected

    assert encode_direct([]) == []
    assert encode_direct(['a']) == [[1, 'a']]
    assert encode_direct(['a', 'a']) == [[2, 'a']]
    assert encode_direct(['a', 'b']) == [[1, 'a'], [1, 'b']]
    assert encode_direct(['a', 'b', 'b']) == [[1, 'a'], [2, 'b']]
