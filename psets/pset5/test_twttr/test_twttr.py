from twttr import shorten

def test_assert():
    assert shorten("hello there") == "hll thr"
    assert shorten("HELLO THERE") == "HLL THR"
    assert shorten("h3ll0 th3r3") == "h3ll0 th3r3"
    assert shorten("h@llo th#r#!") == "h@ll th#r#!"
