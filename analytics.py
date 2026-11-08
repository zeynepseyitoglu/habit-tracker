"""Pure function for analysing habits.

Every function receives habits as input and returns a result.
"""

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