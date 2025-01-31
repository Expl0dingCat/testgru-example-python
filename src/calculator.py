from typing import List, Union
import math

class Calculator:
    def __init__(self, precision: int = 2):
        self.precision = precision
        self._history: List[float] = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers and store the result in history."""
        result = round(a + b, self.precision)
        self._history.append(result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide two numbers with error handling."""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = round(a / b, self.precision)
        self._history.append(result)
        return result

    def calculate_series_sum(self, numbers: List[float]) -> float:
        """Calculate the sum of a series of numbers."""
        if not numbers:
            return 0.0
        result = round(sum(numbers), self.precision)
        self._history.append(result)
        return result

    def get_history(self) -> List[float]:
        """Return the history of calculations."""
        return self._history.copy()

    def calculate_compound_interest(self, principal: float, rate: float, time: float) -> float:
        """
        Calculate compound interest.
        
        Args:
            principal: Initial amount
            rate: Interest rate (as decimal)
            time: Time period in years
        """
        if any(x < 0 for x in [principal, rate, time]):
            raise ValueError("All parameters must be non-negative")
        
        result = round(principal * (1 + rate) ** time, self.precision)
        self._history.append(result)
        return result 