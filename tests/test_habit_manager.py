"""Tests for habit manager."""

import pytest

from habit import Habit, Periodicity
from habit_manager import HabitManager


def test_add_habit_then_find_it():
    manager = HabitManager()
    water = Habit("water", "drink 2 liters", Periodicity.DAILY)

    manager.add_habit(water)

    assert manager.find_habit("water") is water

def test_duplicate_name_is_refused():
    manager = HabitManager(
        [Habit("water", "drink 2 liters", Periodicity.DAILY)]
    )

    with pytest.raises(ValueError):
        manager.add_habit(Habit('water', 'drink 2 liters', Periodicity.WEEKLY))

def test_delete_existing_habit_returns_true():
    manager = HabitManager(
        [Habit("water", "drink 2 liters", Periodicity.DAILY)]
    )

    result = manager.delete_habit("water")

    assert result is True
    assert manager.get_all() == []

def test_delete_missing_habit_returns_false():
    manager = HabitManager([])
    
    result = manager.delete_habit('water')

    assert result is False 