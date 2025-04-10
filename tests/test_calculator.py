import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(1.5, 2.5) == 4.0

def test_add_precision():
    calc = Calculator(precision=3)
    assert calc.add(1.2345, 2.3456) == 3.580

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3.0

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError) as exc_info:
        calc.divide(5, 0)
    assert str(exc_info.value) == "Division by zero is not allowed"

def test_calculate_series_sum():
    calc = Calculator()
    assert calc.calculate_series_sum([1, 2, 3]) == 6.0
    assert calc.calculate_series_sum([]) == 0.0
    assert calc.calculate_series_sum([1.5, 2.5, 3.5]) == 7.5

def test_get_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.divide(6, 2)
    calc.calculate_series_sum([1, 2, 3])
    history = calc.get_history()
    assert history == [5.0, 3.0, 6.0]
    # Verify history is a copy
    history.append(10.0)
    assert len(calc.get_history()) == 3

def test_compound_interest():
    calc = Calculator()
    assert calc.calculate_compound_interest(1000, 0.05, 2) == 1102.5
    assert calc.calculate_compound_interest(100, 0.1, 1) == 110.0

def test_compound_interest_negative_values():
    calc = Calculator()
    with pytest.raises(ValueError) as exc_info:
        calc.calculate_compound_interest(-1000, 0.05, 2)
    assert str(exc_info.value) == "All parameters must be non-negative"

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(1000, -0.05, 2)

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(1000, 0.05, -2)

def test_precision():
    calc = Calculator(precision=4)
    assert calc.add(1.23456, 2.34567) == 3.5802
    assert calc.divide(10, 3) == 3.3333
    assert calc.calculate_series_sum([1.23456, 2.34567]) == 3.5802
    assert calc.calculate_compound_interest(1000, 0.05, 2) == 1102.5000
