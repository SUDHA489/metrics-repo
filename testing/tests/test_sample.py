from files.add import add
from files.sub import sub


def test_addition():
    assert add(1,1) == 2
    assert add(5,4) == 8

def test_subtraction():
    assert sub(5,3) == 2