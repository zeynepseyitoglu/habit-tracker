"""Pure function for analysing habits.

Every function receives habits as input and returns a result.
"""
from datetime import datetime

from habit import Habit, Periodicity


def tracked_habit_names(habits: list[Habit]) -> list[str]:
    """Return the names of all currently tracked habits.

    Args:
        habits: The habits to list.

    Returns:
        The habit names, in the same order as the habits.
    """   
    return [h.name for h in habits]


def habits_by_periodicity(habits: list[Habit], periodicity: Periodicity) -> list[Habit]:
    """Return only the habits with the given periodicity.

    Args:
        habits: The habits to filter.
        periodicity: The periodicity to keep, e.g. Periodicity.WEEKLY.

    Returns:
        A new list containing the matching habits, in their original order.
    """
    return [h for h in habits if h.periodicity == periodicity]


def period_label(when: datetime, periodicity: Periodicity):
    """Return the label of the period (the "box") a check-off falls in.

    Two check-offs share a box exactly when their labels are equal.

    Args:
        when: When the habit was checked off.
        periodicity: How often the habit repeats.

    Returns:
        The date for daily habits, (year, ISO week) for weekly habits,
        and (year, month) for monthly habits.
    """
    if periodicity == Periodicity.DAILY:
        return when.date()
    if periodicity == Periodicity.WEEKLY:
        year, week, weekday = when.isocalendar()
        return (year, week)
    return (when.year, when.month)

def period_number(when: datetime, periodicity: Periodicity) -> int:
    """Return a number identifying the period (the "box") a check-off falls in.

    Consecutive periods always have consecutive numbers, even across
    months and years, so a streak is a run of numbers that differ by 1.

    Args:
        when: When the habit was checked off.
        periodicity: How often the habit repeats.

    Returns:
        A whole number for the day, week or month of ``when``.
    """
    if periodicity == Periodicity.DAILY:
        return when.date().toordinal()
    if periodicity == Periodicity.WEEKLY:
        return (when.date().toordinal() - when.weekday()) // 7
    return when.year * 12 + when.month