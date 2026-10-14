"""Definition of Periodicity and Habits."""

from enum import Enum


class Periodicity(Enum):
    """How often a habit must be done."""

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'