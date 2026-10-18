"""Definition of Periodicity and Habits."""

from enum import Enum
from datetime import datetime


class Periodicity(Enum):
    """How often a habit must be done."""

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'


class Habit:
    """A task a user wants to repeat regularly.

    Each check-off is stored as a timestamp in ``completions``, which acts as the habit's event log. 
    Streaks are calculated using this log by the analytics module.

    Attributes: 
        name: A short label for the habit.
        description: The task specification.
        periodicity: How often the habit is performed.
        created_at: Timestamp of creation time.
        completions: Event log of timestamps for every check-off time."""

    def __init__(self, name: str, description: str, periodicity: Periodicity, created_at: datetime | None = None) -> None:
        """Create a new habit with an empty completions list.
        
        Args:
            ``name``: A short label for the habit, e.g. 'Water'.
            ``description``: The task specification, e.g. 'Drink 2 liters'.
            ``periodicity``: How often the habit is performed.
            ``created_at``: Timestamp of creation time. Defaults to now.
            Pass an earlier datetime to create example data.
        """
        if not isinstance(periodicity, Periodicity):
            raise TypeError('``periodicity`` must be of type ``Periodicity``.')

        if created_at is None:
            created_at = datetime.now()

        if not isinstance(created_at, datetime):
            raise TypeError('``created_at`` must be a ``datetime``.')
        
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.created_at = created_at
        self.completions = []

    def check_off(self, when: datetime | None = None) -> None:
        """Record that the habit was completed.
        
        Adds a timestamp to the habit's event log. A habit can be checked off 
        many times. Extra check-offs in the same period still count as a single 
        completed period.
        
        Args:
            ``when``: When the habit was completed. Defaults to now.
            Pass an earler datetime to log a missed check-off or to create example data."""

        if when is None:
            when = datetime.now()

        if not isinstance(when, datetime):
            raise TypeError('``when`` must be a datetime')
        
        self.completions.append(when)

#Note to self for future features:
#Maybe add: reset completions and uncheck.
