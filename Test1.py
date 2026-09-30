from calculator import add

def test_add():
    answer = add(10, 20)
    assert answer == 30
