import mathlib
import pytest

@pytest.fixture
def cur():
    result = "waiting for user.."
    return result


@pytest.mark.parametrize("a,b,res",[(1,2,3),(3,4,7),(6,2,8)])
def test_addnumbers(a,b,res):
    result = mathlib.addnumbers(a,b)
    assert result == res



def test_printmessage(cur):
    print(cur)
    assert cur == "waiting for user.."

@pytest.mark.skip(reason="I dont want to run this test..")
def test_printmessage2(cur):
    print(cur)
    assert cur == "waiting for user.."