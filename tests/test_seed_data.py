"""Tests for the predefined example habits."""


def test_there_are_five_predefined_habits(predefined_habits):
    assert len(predefined_habits) == 5