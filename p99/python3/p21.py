
# insert an element at a given position into a list

def insert_at(e, n, l):
    if n < 0:
        l = l[::-1]
        n = -1*n-1
        r = l[0:n] + [e] + l[n:]
        return r[::-1]
    return l[0:n] + [e] + l[n:]


def test_insert_at():

    l = ['a', 'b', 'c', 'd']
    l_copy = [e for e in l]
    assert insert_at('new', 1, l) == ['a', 'new', 'b', 'c', 'd']
    assert l == l_copy

    assert insert_at('new', 0, []) == ['new']
    assert insert_at('new', 1, []) == ['new']
    assert insert_at('new', 10, []) == ['new']
    assert insert_at('new', -1, ['a']) == ['a', 'new']
    assert insert_at('new', -2, ['a', 'b']) == ['a', 'new', 'b']
