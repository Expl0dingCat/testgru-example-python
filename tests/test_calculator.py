import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(1.5, 2.5) == 4.0

def test_add_precision():
    calc = Calculator(precision=3)
    assert calc.add(1.2345, 2.3456) == 3.58

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3.0

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as exc:
        calc.divide(5, 0)
    assert str(exc.value) == "Division by zero is not allowed"

def test_calculate_series_sum():
    calc = Calculator()
    assert calc.calculate_series_sum([1, 2, 3, 4]) == 10.0
    assert calc.calculate_series_sum([]) == 0.0
    assert calc.calculate_series_sum([1.5, 2.5, 3.5]) == 7.5

def test_calculate_series_sum_precision():
    calc = Calculator(precision=1)
    assert calc.calculate_series_sum([1.23, 2.34, 3.45]) == 7.0

def test_get_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.divide(10, 2)
    calc.calculate_series_sum([1, 2, 3])
    assert calc.get_history() == [5.0, 5.0, 6.0]

def test_get_history_empty():
    calc = Calculator()
    assert calc.get_history() == []

def test_compound_interest():
    calc = Calculator()
    assert calc.calculate_compound_interest(1000, 0.05, 2) == 1102.5
    assert calc.calculate_compound_interest(100, 0, 5) == 100.0

def test_compound_interest_negative_values():
    calc = Calculator()
    with pytest.raises(ValueError) as exc:
        calc.calculate_compound_interest(-100, 0.05, 2)
    assert str(exc.value) == "All parameters must be non-negative"

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(100, -0.05, 2)

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(100, 0.05, -2)

def test_compound_interest_precision():
    calc = Calculator(precision=4)
    assert calc.calculate_compound_interest(1000, 0.05, 3) == 1157.6250
