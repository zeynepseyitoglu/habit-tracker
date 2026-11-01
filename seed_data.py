"""Predefined example habits with four weeks of tracking data."""

from datetime import datetime, timedelta

from habit import Habit, Periodicity
from storage import save_habits


def create_predefined_habits(today: datetime | None = None) -> list[Habit]:
    """Create the five predefined habits with four
    weeks of check-offs.
    
    The data counts bak from ``today``, so it alwas ends on the current date.
    Tests pass a fixed date to ge predictable results.
    
    Args:
        today: The last day of example data. Defaut to now.
        
    Returns:
        Five habits, each created four weeks before ``today``.
    """

    if today is None:
        today = datetime.now()
    created = today - timedelta(days= 27)

    water = Habit("Drink water", "Drink 2 liters of water", Periodicity.DAILY, created)
    for i in range(28):
        water.check_off(today-timedelta(days=i))

    stretch = Habit("Stretch", "Stretch for 10 minutes", Periodicity.DAILY, created)
    skipped =  {8, 9, 10}
    for i in range(28):
        if i not in skipped:
            stretch.check_off(today - timedelta(days=i))

    bathroom = Habit("Clean bathroom", "Clean the whole bathroom", Periodicity.WEEKLY, created)
    for i in range(0, 28, 7):
        bathroom.check_off(today - timedelta(days=i))

    run = Habit("Go for a run", "Run for at least 20 minutes", Periodicity.WEEKLY, created)
    for i in [0, 2, 7, 9, 11, 21]:
        run.check_off(today - timedelta(days=i))

    budget = Habit("Review budget", "Go through this month's spending", Periodicity.MONTHLY, created)
    budget.check_off(today - timedelta(days=2))

    return [water, stretch, bathroom, run, budget]

if __name__ == "__main__":
    save_habits(create_predefined_habits(), "habits.json")
    print(
        "Saved 5 example habits to habits.json."
    )