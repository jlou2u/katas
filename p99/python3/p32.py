

def gcd(i, j):
    for n in reversed(range(max(i, j)+1)):
        if i % n == 0 and j % n == 0:
            return n


def test_gcd():
    assert gcd(36, 63) == 9
    assert gcd(36, 36) == 36
    assert gcd(36, 37) == 1
    assert gcd(36, 38) == 2
    assert gcd(1, 1) == 1
    assert gcd(3, 9) == 3
