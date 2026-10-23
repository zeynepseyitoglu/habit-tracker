"""Saving and loading habits from/to a JSON file"""

import json
from datetime import datetime

from habit import Habit, Periodicity


def habit_to_dict(habit: Habit) -> dict:
    """Convert a habit into a dictionary that can be saved in JSON.
    
    Datetimes become ISO text and Periodicity becomes its text value
    due to JSON type limitations.
    
    Args:
        habit: The habit to convert.
        
    Returns:
        A dictionary containing only text and lists of text.
    """
    return {
        "name": habit.name,
        "description": habit.description,
        "periodicity": habit.periodicity.value,
        "created_at": habit.created_at.isoformat(),
        "completions": [t.isoformat() for t in habit.completions]     
    }


def dict_to_habit(data: dict) -> Habit:
    """Rebuild a Habit from a dictionary loaded from JSON.

    This is the reverse of ``habit_to_dict``: text values are turned
    back into a Periodicity and datetimes.

    Args:
        data: A dictionary in the format produced by ``habit_to_dict``.

    Returns:
        A Habit with the same values and completions as the original.
    """
    habit = Habit(
        data["name"],
        data["description"],
        Periodicity(data["periodicity"]),
        datetime.fromisoformat(data["created_at"]),    
    )
    habit.completions = [datetime.fromisoformat(s) for s in data["completions"]]
    return habit