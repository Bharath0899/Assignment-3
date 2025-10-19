"""
funcs.py contains five math functions.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a * 1.0 / b

def area_of_square(side: float) -> float:
    """
    Returns the area of a square given a side length.
    """
    return side * side