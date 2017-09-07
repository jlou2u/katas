
# flatten a nested list structure
# note: specificially checks for list to prevent strings or any iterable
#       from being flattened

def flatten(l):
    def _flatten(sl):
        for e in sl:
            if not isinstance(e, list):
                yield e
            else:
                for q in flatten(e):
                    yield q
    return list(_flatten(l))


def test_flatten():

    l = []
    assert flatten(l) == []

    l = [[], [], [[[[[], [], []]], []]]]
    assert flatten(l) == []

    l = [[], [], [[[[[], [], [1]]], []]]]
    assert flatten(l) == [1]

    l = [[], [], [[[[[], [], [None]]], []]]]
    assert flatten(l) == [None]

    l = [[], [], [[[[[], [], ["hello"]]], ["world"]]]]
    assert flatten(l) == ["hello", "world"]

    l = [[1, 1], 2, [3, [5, 8]]]
    assert flatten(l) == [1, 1, 2, 3, 5, 8]
