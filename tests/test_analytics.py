"""Test for the analytic functions."""
import pytest

from analytics import (
    habits_by_periodicity,
    longest_streak_for,
    longest_streak_overall,
    tracked_habit_names,
)
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


def test_longest_streak_for_each_predefined_habit(predefined_habits):
    streaks = [longest_streak_for(h) for h in predefined_habits]

    assert streaks == [28, 17, 4, 2, 1]


def test_longes_streak_overall_is_drink_water(predefined_habits):
    assert longest_streak_overall(predefined_habits) == 28