import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(1.5, 2.5) == 4.0
    assert calc.add(0.1, 0.2) == 0.3

def test_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3.0

    with pytest.raises(ValueError) as exc_info:
        calc.divide(1, 0)
    assert str(exc_info.value) == "Division by zero is not allowed"

def test_calculate_series_sum():
    calc = Calculator()
    assert calc.calculate_series_sum([1, 2, 3]) == 6.0
    assert calc.calculate_series_sum([]) == 0.0
    assert calc.calculate_series_sum([1.5, 2.5, 3.5]) == 7.5
    assert calc.calculate_series_sum([-1, 1]) == 0.0

def test_get_history():
    calc = Calculator()
    calc.add(2, 3)
    calc.divide(6, 2)
    calc.calculate_series_sum([1, 2, 3])

    history = calc.get_history()
    assert history == [5.0, 3.0, 6.0]

    # Test that history is a copy
    history.append(10.0)
    assert len(calc.get_history()) == 3

def test_calculate_compound_interest():
    calc = Calculator()
    assert calc.calculate_compound_interest(1000, 0.05, 2) == 1102.5
    assert calc.calculate_compound_interest(100, 0, 5) == 100.0

    with pytest.raises(ValueError) as exc_info:
        calc.calculate_compound_interest(-100, 0.05, 2)
    assert str(exc_info.value) == "All parameters must be non-negative"

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(100, -0.05, 2)

    with pytest.raises(ValueError):
        calc.calculate_compound_interest(100, 0.05, -2)

def test_precision():
    calc = Calculator(precision=3)
    assert calc.add(1/3, 1/3) == 0.667
    assert calc.divide(1, 3) == 0.333
    assert calc.calculate_series_sum([1/3, 1/3, 1/3]) == 1.0
    assert calc.calculate_compound_interest(100, 0.1, 2) == 121.0

def test_large_numbers():
    calc = Calculator()
    assert calc.add(1e6, 2e6) == 3e6
    assert calc.divide(1e6, 2) == 5e5
    assert calc.calculate_series_sum([1e6, 2e6, 3e6]) == 6e6
    assert calc.calculate_compound_interest(1e6, 0.1, 1) == 1.1e6

def test_small_numbers():
    calc = Calculator(precision=10)
    assert calc.add(1e-6, 2e-6) == 3e-6
    assert calc.divide(1e-6, 2) == 5e-7
    assert calc.calculate_series_sum([1e-6, 2e-6, 3e-6]) == 6e-6
    assert calc.calculate_compound_interest(1e-6, 0.1, 1) == 1.1e-6
