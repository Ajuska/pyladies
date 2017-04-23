def secti(a, b):
    return a + b
# normalne se importi --- from secti import secti
from pytest import raises


def test_secti():
    assert secti(2, 3) == 5

def test_secti_error():
    with raises(TypeError):
        assert secti(2, 'a')
