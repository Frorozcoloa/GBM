import pytest
from jumping_count import jumping_count, get_numbers, get_first_value
from io import StringIO
from unittest.mock import patch

def test_jumping_count():
    assert jumping_count(10) == 4
    assert jumping_count(15) == 5
    assert jumping_count(100) == 14
    assert jumping_count(20) == 7


def test_examples():
    assert jumping_count(1) == 1
    assert jumping_count(2) == 3
    assert jumping_count(3) == 2
    assert jumping_count(4) == 3
    assert jumping_count(5) == 4

@pytest.mark.parametrize(
    "input_value_first, expected_output_first, input_value_second, expected_output_second",
    [
        ('5\n', 5, '0\n', pytest.raises(ValueError)),
        ('5\n', 5, '1200\n', pytest.raises(ValueError)),
        ('0\n', pytest.raises(ValueError), '1200\n', pytest.raises(ValueError)),
    ]
)
def test_get_first_value(input_value_first, expected_output_first, input_value_second, expected_output_second, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: input_value_first)
        if isinstance(expected_output_first, int):
            assert get_first_value() == expected_output_first
        else:
            with expected_output_first:
                get_first_value()

        m.setattr('builtins.input', lambda _: input_value_second)
        if isinstance(expected_output_second, int):
            assert get_first_value() == expected_output_second
        else:
            with expected_output_second:
                get_first_value()

@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ('10\n', (10, False)),
        ('200\n', (200, True)),
    ]
)
def test_get_numbers(input_value, expected_output, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr('builtins.input', lambda _: input_value)
        assert get_numbers() == expected_output