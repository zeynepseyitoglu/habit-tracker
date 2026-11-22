"""Interactive menu for the habit tracker."""

import click

from habit_manager import HabitManager
from storage import load_habits, save_habits

HABITS_FILE = 'habits.json'


@click.command()
def main():
    """Start the main habit tracker menu."""
    manager = HabitManager(load_habits(HABITS_FILE))
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

        if choice == 6:
            click.echo("Goodbye! Your habits are saved.")
            break


if __name__ == "__main__":
    main()