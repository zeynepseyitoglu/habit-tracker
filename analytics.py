"""Pure function for analysing habits.

Every function receives a habit as input and returns a result.
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

