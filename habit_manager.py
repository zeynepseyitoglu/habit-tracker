"""Managing the collection of habits."""

from habit import Habit


class HabitManager:
    """Keeps track of all habits. Allows for the following operations:
    add, find, and delete habits.
    
    The manager does not read or write files. The caller loads the habits
    with ``storage.load_habits`` and passes them in.
    
    Attributes:
        habits: Every habit currently being tracked.
    """

    def __init__(self, habits: list[Habit] | None = None) -> None:
        """Create a manager for the habits.
        
        Args:
            habits: The habits to manage. Defaults to an
            empty list.
        """
        if habits is None:
            habits = []
        self.habits = habits

    def get_all(self) -> list[Habit]:
        """return a copy of thelist of every habit that is
        being tracked."""
        return list(self.habits)

    def find_habit(self, name: str) -> Habit | None:
        """Checks each habit in the list to find the corresponding habit
        and returns that habit.
        
        Args: 
            name: name of the habit that wants to be found.
            
        returns: 
            habit: the habit object or None if no habit by that name exists.
            """
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit

        return None

    def add_habit(self, habit: Habit) -> None:
        """Adds a new habit to be tracked.

        Names must be unique, ignoring capital letters.

        Args:
            habit: the habit to add.
        
        Raises:
            ValueError: If a habit with the same name already exists.
        """
        if self.find_habit(habit.name) is not None:
            raise ValueError(f"A habit called '{habit.name}' already exists.")
        self.habits.append(habit)
