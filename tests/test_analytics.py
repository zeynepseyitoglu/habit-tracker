"""Test for the analytic functions."""
import pytest

from analytics import (
    habits_by_periodicity,
    longest_streak_for,
    longest_streak_overall,
    tracked_habit_names,
)
from datetime import datetime, timedelta
from habit import Habit, Periodicity


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


def make_habit(periodicity, dates):
    """Build a test habit checked off at the given dates."""
    habit = Habit("Test", "A test habit", periodicity, datetime(2026, 1, 1))
    for when in dates:
        habit.check_off(when)
    return habit

#------ Edge cases ---------

def test_no_check_offs_gives_zero():
    habit = make_habit(Periodicity.DAILY, [])
    assert longest_streak_for(habit) == 0


def test_one_check_off_gives_one():
    habit = make_habit(Periodicity.DAILY, [datetime(2026, 3, 1, 8, 0)])
    assert longest_streak_for(habit) == 1


def test_two_check_offs_same_day_count_once():
    habit = make_habit(Periodicity.DAILY, [datetime(2026, 3, 1, 8, 0), datetime(2026, 3, 1, 21, 0)])
    assert longest_streak_for(habit) == 1


def test_check_offs_out_of_order_still_count():
    days = [datetime(2026, 3, 3, 9, 0), datetime(2026, 3, 1, 9, 0), datetime(2026, 3, 2, 9, 0)]
    habit = make_habit(Periodicity.DAILY, days)
    assert longest_streak_for(habit) == 3


def test_weekly_streak_accross_new_year():
    habit = make_habit(Periodicity.WEEKLY, [datetime(2026, 12, 28, 9, 0), datetime(2027, 1, 4, 9, 0)])
    assert longest_streak_for(habit) == 2


def test_monthly_streak_accross_new_year():
    habit = make_habit(Periodicity.MONTHLY, [datetime(2026, 12, 15, 9, 0), datetime(2027, 1, 15, 9, 0)])
    assert longest_streak_for(habit) == 2


def test_streak_longer_than_a_year():
    start = datetime(2026, 1, 1, 9, 0)
    habit = make_habit(Periodicity.DAILY, [start + timedelta(days=i) for i in range(400)])
    assert longest_streak_for(habit) == 400


def test_no_habits_gives_zero_overall():
    assert longest_streak_overall([]) == 0