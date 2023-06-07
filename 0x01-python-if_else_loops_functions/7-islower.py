#!/usr/bin/python3
def islower(c):
    """
    Check whether a character is lowercase.

    Args:
        c (str): The character to be checked.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')
