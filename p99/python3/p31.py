

def is_prime(n):
    if n <= 3:
        return True

    return not any([n % i == 0 for i in range(2, n)])


def test_is_prime():

    assert is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    assert is_prime(17)
    assert is_prime(19)
    assert is_prime(23)
    assert is_prime(29)
    assert is_prime(31)
    assert is_prime(37)
    assert is_prime(41)
    assert is_prime(43)
    assert is_prime(43)
    assert is_prime(97)

    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert not is_prime(12)
    assert not is_prime(14)
    assert not is_prime(96)

