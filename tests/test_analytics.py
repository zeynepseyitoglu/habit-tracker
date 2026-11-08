"""Test for the analytic functions."""
import pytest

from analytics import habits_by_periodicity, tracked_habit_names
from habit import Periodicity


def test_tracked_habit_names_lists_all_five(predefined_habits):
    names = tracked_habit_names(predefined_habits)

    assert names == ["Drink water", "Stretch", "Clean bathroom", "Go for a run", "Review budget"]


@pytest.mark.parametrize("periodicity, expected", [
    (Periodicity.DAILY, ["Drink water", "Stretch"]),
    (Periodicity.WEEKLY, ["Clean bathroom", "Go for a run"]),
    (Periodicity.MONTHLY, ["Review budget"]),
])
def test_habits_by_periodicity(predefined_habits, periodicity, expected):
    names = tracked_habit_names(habits_by_periodicity(predefined_habits, periodicity))
    assert names == expected