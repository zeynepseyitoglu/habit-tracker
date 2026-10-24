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

def  save_habits(habits: list[Habit], path: str) -> None:
    """Save all habits to a JSON file, replacing its previus contents.
    
    Args:
        habits: Every habit that will be saved.
        path: The file to write.
        """

    data = [habit_to_dict(h) for h in habits]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_habits(path:str) -> list[Habit]:
    """Load all habits from a JSON file.
    
    Args:
        path: The file to read from.
        
    Returns:
        The saved habits, or and empty list if the file does not exist.
    """

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return [dict_to_habit(d) for d in data]