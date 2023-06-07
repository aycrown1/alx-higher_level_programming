#!/usr/bin/python3
def print_last_digit(number):
    """
    Print the last digit of a number and return its value.

    Args:
        number (int): The number to extract the last digit from.

    Returns:
        int: The value of the last digit.
    """
    if number >= 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
