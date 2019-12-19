# -*- coding: utf-8 -*-

import pytest
from codeowener_ci.skeleton import fib

__author__ = "Alec Harmon"
__copyright__ = "Alec Harmon"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
