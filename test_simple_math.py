import pytest
from simple_math import SimpleMath

@pytest.fixture()
def s_math():
    return SimpleMath()

def test_square(s_math):
    assert s_math.square(2) == 4

def test_cube(s_math):
    assert s_math.cube(-3) == -27