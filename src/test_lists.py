"""List tests."""


from lists import drop, length, Link

def test_iter() -> None:
    x = iter(Link(1, Link(2, None)))
    assert next(x) == 1
    assert next(x) == 2
    

def test_length() -> None:
    """Write tests if you want them."""
    assert length(None) == 0
    assert length(Link(1, None)) == 1
    assert length(Link(1, Link(2, None))) == 2

def test_drop() -> None:
    assert drop(None, 1) is None
    assert drop(Link(1, None), 1) is None
    #assert drop(Link(1, Link(2, None)), 1) == Link(2, None)