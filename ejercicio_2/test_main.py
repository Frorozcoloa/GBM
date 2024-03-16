import pytest
from io import StringIO
from unittest.mock import patch
from main import get_grand_pilots, result_race, get_total_scoring, get_values_scoring, calculate_champion

# Test get_grand_pilots function
def test_get_grand_pilots_valid_input(monkeypatch):
    input_values = ['5 10']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    assert get_grand_pilots() == (5, 10)

def test_get_grand_pilots_invalid_input(monkeypatch):
    input_values = ['101 10']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    with pytest.raises(ValueError):
        get_grand_pilots()

# Test result_race function
def test_result_race_valid_input(monkeypatch):
    input_values = ['1 2 3']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    assert result_race(1) == [[1, 2, 3]]

def test_result_race_invalid_input(monkeypatch):
    input_values = ['1 a b']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    with pytest.raises(ValueError):
        result_race(1)

# Test get_total_scoring function
def test_get_total_scoring_valid_input(monkeypatch):
    input_values = ['3']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    assert get_total_scoring() == 3

def test_get_total_scoring_invalid_input(monkeypatch):
    input_values = ['0']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    with pytest.raises(ValueError):
        get_total_scoring()

# Test get_values_scoring function
def test_get_values_scoring_valid_input(monkeypatch):
    input_values = ['3 1 10', '2 5 3', '3 4 2 1']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    assert get_values_scoring(10, 3) == [[1, 10], [5, 3], [4, 2, 1]]

def test_get_values_scoring_invalid_input(monkeypatch):
    input_values = ['2 1 10', '3 5 3', '2 4 2 1']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    with pytest.raises(ValueError):
        get_values_scoring(10, 3)

# Test calculate_champion function
def test_calculate_champion():
    pilots = 4
    race_results = [[1, 3, 4, 2], [4, 1, 3, 2]]
    scoring_systems = [[3, 3, 2, 1], [3, 5, 4, 2]]
    assert calculate_champion(pilots, race_results, scoring_systems) == [[2, 4], [4]]

    pilots = 10
    race_results = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]]
    scoring_systems = [[5, 5, 4, 3, 2, 1], [3, 10, 5, 1]]
    assert  calculate_champion(pilots, race_results, scoring_systems) == [[3], [3]]

    P = 3
    race_results = [[3, 2, 1]]
    scoring_systems = [[3, 5, 3, 2], [3, 5, 2, 1], [3, 1, 1, 1]]
    assert calculate_champion(P, race_results, scoring_systems) == [[3], [3], [1, 2, 3]]