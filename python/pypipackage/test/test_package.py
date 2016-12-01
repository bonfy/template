# coding: utf-8

from package.test import plus, minus


def test_plus():
    assert plus(1, 1) == 2
    assert plus(1, -1) == 0


def test_minus():
    assert minus(1, 1) == 0
    assert minus(1, -1) == 2
