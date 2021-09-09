

def gcd(i, j):
    for n in reversed(range(max(i, j)+1)):
        if i % n == 0 and j % n == 0:
            return n

def is_coprime(i, j):
    return gcd(i, j) == 1


def test_gcd():
    assert is_coprime(35, 64)
