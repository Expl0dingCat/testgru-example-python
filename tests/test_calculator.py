import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

def test_add_positive_numbers():
    calc = Calculator()
    result = calc.add(2.5, 3.5)
    assert result == 6.0
    assert calc.get_history() == [6.0]

def test_add_negative_numbers():
    calc = Calculator()
    result = calc.add(-2.5, -3.5)
    assert result == -6.0
    assert calc.get_history() == [-6.0]

def test_add_with_precision():
    calc = Calculator(precision=3)
    result = calc.add(1.2345, 2.3456)
    assert result == 3.58
    assert calc.get_history() == [3.58]

def test_divide_positive_numbers():
    calc = Calculator()
    result = calc.divide(10.0, 2.0)
    assert result == 5.0
    assert calc.get_history() == [5.0]

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10.0, 0)
    assert str(exc_info.value) == "Division by zero is not allowed"
    assert calc.get_history() == []

def test_divide_with_precision():
    calc = Calculator(precision=3)
    result = calc.divide(10.0, 3.0)
    assert result == 3.333
    assert calc.get_history() == [3.333]

def test_calculate_series_sum_empty():
    calc = Calculator()
    result = calc.calculate_series_sum([])
    assert result == 0.0
    assert calc.get_history() == []

def test_calculate_series_sum():
    calc = Calculator()
    result = calc.calculate_series_sum([1.1, 2.2, 3.3])
    assert result == 6.6
    assert calc.get_history() == [6.6]

def test_calculate_series_sum_precision():
    calc = Calculator(precision=1)
    result = calc.calculate_series_sum([1.11, 2.22, 3.33])
    assert result == 6.7
    assert calc.get_history() == [6.7]

def test_get_history_multiple_operations():
    calc = Calculator()
    calc.add(1.0, 2.0)
    calc.divide(6.0, 2.0)
    calc.calculate_series_sum([1.0, 2.0, 3.0])
    assert calc.get_history() == [3.0, 3.0, 6.0]

def test_compound_interest_basic():
    calc = Calculator()
    result = calc.calculate_compound_interest(1000.0, 0.05, 2.0)
    assert result == 1102.5
    assert calc.get_history() == [1102.5]

def test_compound_interest_zero_time():
    calc = Calculator()
    result = calc.calculate_compound_interest(1000.0, 0.05, 0.0)
    assert result == 1000.0
    assert calc.get_history() == [1000.0]

def test_compound_interest_negative_values():
    calc = Calculator()
    with pytest.raises(ValueError) as exc_info:
        calc.calculate_compound_interest(-1000.0, 0.05, 2.0)
    assert str(exc_info.value) == "All parameters must be non-negative"
    assert calc.get_history() == []

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(1000.0, -0.05, 2.0)
    assert calc.get_history() == []

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(1000.0, 0.05, -2.0)
    assert calc.get_history() == []
