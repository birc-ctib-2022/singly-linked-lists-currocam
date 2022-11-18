"""Singly-linked lists."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')  # Generic type variable

class Link(Generic[T]):
    """A link in a singly linked list."""

    head: T
    tail: LList[T]

    def __init__(self, head: T, tail: LList[T]):
        """Prepend a new head to tail."""
        self.head = head
        self.tail = tail

    def __repr__(self) -> str:
        """Representation string."""
        return f'Link({self.head}, {self.tail})'
    def __iter__(self):
        link = self
        while link is not None:
            yield link.head
            link = link.tail
        return StopIteration
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.head != other.head:
            return False
        return self.tail.__eq__(other.tail)        
    def __ne__(self, other):
        return not self.__eq__(other)


LList = Optional[Link[T]]  # A list is just a reference to the head or None


def length(x: LList[T]) -> int:
    """
    Get the length of x.

    >>> length(None)
    0
    >>> length(Link(1, None))
    1
    >>> length(Link(1, Link(2, None)))
    2
    """
    acc = 0
    if x is None:
        return acc
    for _ in x:
        acc += 1
    return acc


def drop(x: LList[T], k: int) -> LList[T]:
    """
    Drop the first k elements in the list.

    If length(x) < k, return the empty list.

    >>> drop(None, 1) is None
    True
    >>> drop(Link(1, None), 1) is None
    True
    >>> drop(Link(1, Link(2, None)), 1)
    Link(2, None)
    """
    for _ in range(k):
        if x is None: return x
        x = x.tail
    return x


def take(x: LList[T], k: int) -> LList[T]:
    """
    Return a list with the first k elements in x.

    If length(x) < k, return the full list. You decide whether you
    want to return a copy of x or the original list.

    >>> take(None, 1) is None
    True
    >>> take(Link(1, None), 1)
    Link(1, None)
    >>> take(Link(1, Link(2, Link(3, None))), 2)
    Link(1, Link(2, None))
    """
    lst = None
    if x is None: return x
    for index, elm in enumerate(x):
        if index == k: break
        lst = add_elm(elm, lst)
    return reverse(lst)

def add_elm(x: T,  lst: LList[T]) -> LList[T]:
    return Link(x, lst)

def reverse(x: LList[T]) -> LList[T]:
    """
    Reverse a list.

    You decide whether you are allowed to modify the existing list
    or if you want to return a new list and leave the original one
    intact.

    >>> reverse(None) is None
    True
    >>> reverse(Link(1, None))
    Link(1, None)
    >>> reverse(Link(1, Link(2, Link(3, None))))
    Link(3, Link(2, Link(1, None)))
    """
    return flip(None, x)

def flip(x: LList[T], y: LList[T]) -> LList[T]:
    if y is None:
        return x
    return flip(Link(y.head, x), y.tail)