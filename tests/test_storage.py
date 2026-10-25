"""Test for persistence of habits."""

from habit import Habit, Periodicity
from storage import load_habits, save_habits


def test_save_then_load_keeps_habit(tmp_path):
    path = tmp_path/"habits.json"
    water = Habit('Water', 'Drink 2 Liters', Periodicity.DAILY)
    water.check_off()

    save_habits([water], path)
    loaded = load_habits(path)

    assert loaded[0].name == "Water"
    assert loaded[0].periodicity == Periodicity.DAILY
    assert loaded[0].completions == water.completions

def test_load_missing_file_gives_empty_list(tmp_path):
    path = tmp_path / "habits.json"
    loaded = load_habits(path)

    assert loaded == []