import pytest
import sys
import os

# Add the src directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add_positive_numbers(calculator):
    result = calculator.add(2.5, 3.5)
    assert result == 6.0
    assert calculator.get_history() == [6.0]

def test_add_negative_numbers(calculator):
    result = calculator.add(-2.5, -3.5)
    assert result == -6.0
    assert calculator.get_history() == [-6.0]

def test_add_zero(calculator):
    result = calculator.add(5.0, 0.0)
    assert result == 5.0
    assert calculator.get_history() == [5.0]

def test_divide_positive_numbers(calculator):
    result = calculator.divide(10.0, 2.0)
    assert result == 5.0
    assert calculator.get_history() == [5.0]

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as exc_info:
        calculator.divide(10.0, 0.0)
    assert str(exc_info.value) == "Division by zero is not allowed"
    assert calculator.get_history() == []

def test_divide_negative_numbers(calculator):
    result = calculator.divide(-10.0, 2.0)
    assert result == -5.0
    assert calculator.get_history() == [-5.0]

def test_calculate_series_sum_empty_list(calculator):
    result = calculator.calculate_series_sum([])
    assert result == 0.0
    # Empty list returns 0.0 but doesn't add to history
    assert calculator.get_history() == []

def test_calculate_series_sum(calculator):
    result = calculator.calculate_series_sum([1.0, 2.0, 3.0, 4.0])
    assert result == 10.0
    assert calculator.get_history() == [10.0]

def test_calculate_series_sum_negative_numbers(calculator):
    result = calculator.calculate_series_sum([-1.0, -2.0, -3.0])
    assert result == -6.0
    assert calculator.get_history() == [-6.0]

def test_get_history_multiple_operations(calculator):
    calculator.add(2.0, 3.0)
    calculator.divide(10.0, 2.0)
    calculator.calculate_series_sum([1.0, 2.0, 3.0])
    assert calculator.get_history() == [5.0, 5.0, 6.0]

def test_compound_interest_positive_values(calculator):
    result = calculator.calculate_compound_interest(1000.0, 0.05, 2.0)
    assert result == 1102.5
    assert calculator.get_history() == [1102.5]

def test_compound_interest_zero_rate(calculator):
    result = calculator.calculate_compound_interest(1000.0, 0.0, 5.0)
    assert result == 1000.0
    assert calculator.get_history() == [1000.0]

def test_compound_interest_negative_values(calculator):
    with pytest.raises(ValueError) as exc_info:
        calculator.calculate_compound_interest(-1000.0, 0.05, 2.0)
    assert str(exc_info.value) == "All parameters must be non-negative"
    assert calculator.get_history() == []

def test_precision(calculator):
    calc = Calculator(precision=4)
    result = calc.add(1.23456, 2.34567)
    assert result == 3.5802
    assert calc.get_history() == [3.5802]
