"""Utility functions for basic arithmetic operations."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of a and b. Raises ZeroDivisionError if b is 0."""
    return a / b


def convert_to_binary(number):
    """Convert a natural number from 0 to 100 to its binary representation."""
    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    if number < 0 or number > 100:
        raise ValueError("Number must be between 0 and 100.")
    return bin(number)
