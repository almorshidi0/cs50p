from bank import value

def test_assert():
    assert value("hello there") == 0
    assert value("HELLO THERE") == 0
    assert value("hi there") == 20
    assert value("there") == 100
