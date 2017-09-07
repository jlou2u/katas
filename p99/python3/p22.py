
# create a list containing all integers within a given range

def rng(i, k):
    return list(range(i, k+1))


def test_rng():

    assert rng(4, 9) == [4, 5, 6, 7, 8, 9]
