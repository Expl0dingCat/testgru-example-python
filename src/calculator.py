"""
A simple calculator module that provides basic arithmetic operations and financial calculations.

This module implements a Calculator class that can perform basic arithmetic operations
like addition and division, as well as more complex calculations like series sums
and compound interest. All calculations are stored in a history for later retrieval.
"""
# test 
from typing import List, Union
import math


class Calculator:
    """
    A calculator class that performs basic arithmetic and financial calculations.
    
    This calculator maintains a history of all calculations performed and allows
    for customizable precision in the results. It provides methods for basic
    arithmetic operations as well as more complex financial calculations.
    
    Attributes:
        precision (int): The number of decimal places to round results to.
        _history (List[float]): A list storing the history of calculation results.
    """
    
    def __init__(self, precision: int = 2):
        """
        Initialize the calculator with specified precision.
        
        Args:
            precision (int, optional): The number of decimal places to round results to.
                                      Defaults to 2.
        """
        self.precision = precision
        self._history: List[float] = []

    def add(self, a: float, b: float) -> float:
        """
        Add two numbers and store the result in history.
        
        Args:
            a (float): The first number.
            b (float): The second number.
            
        Returns:
            float: The sum of a and b, rounded to the specified precision.
        """
        result = round(a + b, self.precision)
        self._history.append(result)
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Divide two numbers with error handling.
        
        Args:
            a (float): The numerator.
            b (float): The denominator.
            
        Returns:
            float: The quotient of a divided by b, rounded to the specified precision.
            
        Raises:
            ValueError: If b is zero (division by zero).
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        result = round(a / b, self.precision)
        self._history.append(result)
        return result

    def calculate_series_sum(self, numbers: List[float]) -> float:
        """
        Calculate the sum of a series of numbers.
        
        Args:
            numbers (List[float]): A list of numbers to sum.
            
        Returns:
            float: The sum of all numbers in the list, rounded to the specified precision.
                  Returns 0.0 if the list is empty.
        """
        if not numbers:
            return 0.0
        result = round(sum(numbers), self.precision)
        self._history.append(result)
        return result

    def get_history(self) -> List[float]:
        """
        Return the history of calculations.
        
        Returns:
            List[float]: A copy of the calculation history.
        """
        return self._history.copy()

    def calculate_compound_interest(self, principal: float, rate: float, time: float) -> float:
        """
        Calculate compound interest.
        
        This method calculates the future value of an investment with compound interest
        using the formula: A = P(1 + r)^t, where:
        - A is the amount of money accumulated after n years, including interest
        - P is the principal amount (the initial amount of money)
        - r is the annual interest rate (in decimal form)
        - t is the time the money is invested for in years
        
        Args:
            principal (float): Initial amount of money invested.
            rate (float): Annual interest rate as a decimal (e.g., 0.05 for 5%).
            time (float): Time period in years.
            
        Returns:
            float: The future value of the investment, rounded to the specified precision.
            
        Raises:
            ValueError: If any of the parameters are negative.
        """
        if any(x < 0 for x in [principal, rate, time]):
            raise ValueError("All parameters must be non-negative")
        
        result = round(principal * (1 + rate) ** time, self.precision)
        self._history.append(result)
        return result 