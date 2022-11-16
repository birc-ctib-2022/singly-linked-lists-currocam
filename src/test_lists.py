"""List tests."""


from lists import drop, length, Link, take

def test_iter() -> None:
    x = iter(Link(1, Link(2, None)))
    assert next(x) == 1
    assert next(x) == 2
    
def test_equal() -> None:
    assert Link(1, Link(2, None)) == Link(1, Link(2, None))
    assert Link(1, None) == Link(1, None)
    assert Link(1, Link(2, None)) != Link(1, None)
    assert Link(1, Link(2, None)) != 3


def test_length() -> None:
    """Write tests if you want them."""
    assert length(None) == 0
    assert length(Link(1, None)) == 1
    assert length(Link(1, Link(2, None))) == 2

def test_drop() -> None:
    assert drop(None, 1) is None
    assert drop(Link(1, None), 1) is None
    assert drop(Link(1, Link(2, None)), 1) == Link(2, None)


def test_take() -> None:
    assert take(None, 1) is None
    assert take(Link(1, None), 1) == Link(1, None)
    assert take(Link(1, Link(2, Link(3, None))), 2) == Link(1, Link(2, None))