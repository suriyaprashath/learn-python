"""
Advanced Calculator Operations
Provides advanced mathematical functions.
"""

import math

def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent

def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(number)

def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers!")
    return math.factorial(n)
