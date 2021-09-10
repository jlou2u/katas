
import itertools

def group(n, l, acc=[]):
    if len(n) == 0:
        return acc
    results = []
    for item in list(itertools.combinations(l, n[0])):
        rem = [z for z in l if z not in item]
        result = group(n[1:], rem, acc + [list(item)])
        results.append(result)
    if len(n) == 1:
        return results[0]
    else:
        return results

def test_group2():
    result = group([1, 2], ['A', 'B', 'C'])
    expected = [
        [['A'], ['B', 'C']],
        [['B'], ['A', 'C']],
        [['C'], ['A', 'B']]
    ]
    assert expected == result


def test_group3():
    result = group([1, 1, 1], ['A', 'B', 'C'])

    expected = [
        [[['A'], ['B'], ['C']], [['A'], ['C'], ['B']]],
        [[['B'], ['A'], ['C']], [['B'], ['C'], ['A']]],
        [[['C'], ['A'], ['B']], [['C'], ['B'], ['A']]]
    ]

    assert expected == result
