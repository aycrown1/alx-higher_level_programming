#!/usr/bin/python3
def uppercase(str):
    """
    Prints a string in uppercase
    Args:
        s (str): The string to be printed in uppercase.

    Returns:
        None
    """
    for c in str:
        print("{}".format(chr(ord(c) - 32)), end='')
    print()
