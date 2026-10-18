"""Tests for Habit class."""

from datetime import datetime

from habit import Habit, Periodicity


def test_new_habit_no_completions():
    water = Habit('Water', 'Drink 2 Liters', Periodicity.DAILY)
    assert water.completions == []


def test_check_off_adds_log():
    cook = Habit('Cook a meal', 'Cook a homemade meal', Periodicity.WEEKLY)
    cook.check_off()

    assert len(cook.completions) == 1


def test_check_off_accepts_a_past_date():
    past = datetime(2026, 10, 1, 9, 0)
    clean = Habit('Clean', 'Tidy a little each night', Periodicity.DAILY)

    clean.check_off(past)

    assert clean.completions == [past]