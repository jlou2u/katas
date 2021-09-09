

def gcd(i, j):
    for n in reversed(range(max(i, j)+1)):
        if i % n == 0 and j % n == 0:
            return n

def is_coprime(i, j):
    return gcd(i, j) == 1


def totient(m):
    n = 0
    for i in reversed(range(m+1)):
        if is_coprime(m, i):
            n = n + 1
    return n


def test_totient():
    assert totient(2) == 1
    assert totient(3) == 2
    assert totient(4) == 2
    assert totient(5) == 4
    assert totient(6) == 2
    assert totient(7) == 6
    assert totient(8) == 4
    assert totient(9) == 6
    assert totient(10) == 4
    assert totient(11) == 10
    assert totient(12) == 4
    assert totient(13) == 12
    assert totient(14) == 6
    assert totient(15) == 8
