"""Shared test data for all test files."""

from datetime import datetime

import pytest

from seed_data import create_predefined_habits


@pytest.fixture
def predefined_habits():
    """The five predefined habits, ending on a fixed date."""
    return create_predefined_habits(datetime(2026, 10, 31, 12, 0))