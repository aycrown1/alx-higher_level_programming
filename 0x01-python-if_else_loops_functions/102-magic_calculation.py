#!/usr/bin/python3
def magic_calculation(a, b, c):
    """
    Perform a magic calculation based on the given parameters.

    The function takes three parameters: a, b, and c.
    It performs a series of comparisons and arithmetic operations
    to determine the result of the magic calculation.

    Args:
        a (int): The first input parameter.
        b (int): The second input parameter.
        c (int): The third input parameter.

    Returns:
        int: The result of the magic calculation.

    """

    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return (a * b) - c
