"""Interactive menu for the habit tracker."""

import click

from datetime import datetime, timedelta
from habit import Habit, Periodicity
from habit_manager import HabitManager
from seed_data import create_predefined_habits
from analytics import habits_by_periodicity, longest_streak_overall, longest_streak_for
from storage import load_habits, save_habits

HABITS_FILE = 'habits.json'


def add_habit_from_menu(manager: HabitManager) -> None:
    """Ask for a new habit's details, add it and save."""
    name = click.prompt("Name").strip()
    description = click.prompt('Description').strip()
    periodicity = click.prompt(
        "Periodicity",
        type=click.Choice(["daily", "weekly", "monthly"], case_sensitive=False),
        default="daily",
    )
    habit = Habit(name, description, Periodicity(periodicity.lower()))
    try:
        manager.add_habit(habit)
    except ValueError as error:
        click.echo(error)
        return
    save_habits(manager.get_all(), HABITS_FILE)
    click.echo(f'Added "{name}" ({periodicity}).')


def choose_habit(manager: HabitManager, question: str) -> Habit | None:
    """Show the habits as a numbered list and return the one the user picks.
    
    Returns None if there are no habits.
    """
    habits = manager.get_all()
    if not habits:
        click.echo("You have no habits yet.")
        return None
    click.echo(question)
    for number, habit in enumerate(habits, start=1):
        click.echo(f" {number}) {habit.name}")
    choice = click.prompt("Choose", type=click.IntRange(1, len(habits)))
    return habits[choice - 1]


def check_off_from_menu(manager: HabitManager) -> None:
    """Let user pick a habit and check it off, today or a recent day.
    """
    habit = choose_habit(manager, "Which habit did you do?")
    if habit is None:
        return
    days_ago = click.prompt(
        "How many days ago? (0 = today)", type=click.IntRange(0, 7), default=0
    )
    habit.check_off(datetime.now() - timedelta(days=days_ago))
    save_habits(manager.get_all(), HABITS_FILE)
    click.echo(f'Checked off "{habit.name}". Nice work!')


def show_habits_from_menu(manager: HabitManager) -> None:
    """List the habits, either all of them or only one."""
    which = click.prompt(
        "Show which habits?",
        type=click.Choice(['all', 'daily', 'weekly', 'monthly'], case_sensitive=False),
        default='all'
    )
    habits = manager.get_all()
    if which.lower() != "all":
        habits = habits_by_periodicity(habits, Periodicity(which.lower()))
    if not habits:
        click.echo("No habits to show.")
        return
    for habit in habits:
        click.echo(f' - {habit.name} ({habit.periodicity.value}): {habit.description}')


def show_streaks_from_menu(manager:HabitManager) -> None:
    """Show each habit's longest streak and the best streak overall."""
    habits = manager.get_all()
    if not habits:
        click.echo("You have no habits yet.")
        return
    for habit in habits:
        click.echo(f' - {habit.name}: longest streak {longest_streak_for(habit)} ({habit.periodicity.value}).')
    click.echo(f'Best streak overall among all habits: {longest_streak_overall(habits)}.')


def delete_habit_from_menu(manager: HabitManager) -> None:
    """Let the user pick a habit and delete it after confirming."""
    habit = choose_habit(manager, "Which habit should be deleted?")
    if habit is None:
        return
    if click.confirm(f'Delete "{habit.name}" and all its history?'):
        manager.delete_habit(habit.name)
        save_habits(manager.get_all(), HABITS_FILE)
        click.echo(f'Deleted "{habit.name}".')
    else:
        click.echo("Nothing deleted.")


@click.command()
def main():
    """Start the main habit tracker menu."""
    habits = load_habits(HABITS_FILE)
    if not habits and click.confirm("No habits yet. Load 5 example habits with 4 weeks of data?"):
        habits = create_predefined_habits()
        save_habits(habits, HABITS_FILE)

    manager = HabitManager(habits)
    click.echo("welcome to Habit Tracker!")

    while True:
        click.echo("\nWhat would you like to do?")
        click.echo("  1) Add a habit")
        click.echo("  2) Check off a habit")
        click.echo("  3) See my habits")
        click.echo("  4) See my streaks")
        click.echo("  5) Delete a habit")
        click.echo("  6) Quit")
        choice = click.prompt("Choose", type=click.IntRange(1, 6))

        if choice == 1:
            add_habit_from_menu(manager)
        elif choice == 2:
            check_off_from_menu(manager)
        elif choice == 3:
            show_habits_from_menu(manager)
        elif choice == 4:
            show_streaks_from_menu(manager)
        elif choice == 5:
            delete_habit_from_menu(manager)
        elif choice == 6:
            click.echo("Goodbye! Your habits are saved.")
            break


if __name__ == "__main__":
    main()