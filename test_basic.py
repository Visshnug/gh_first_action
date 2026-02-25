import pytest
from basic import greet


def test_greet_returns_correct_message():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_empty_name():
    assert greet("") == "Hello, !"
