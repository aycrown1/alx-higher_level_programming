#!/usr/bin/python3
def uppercase(str):
    """
    output a string in uppercase
    Args:
        str (str): The string to be outputed in uppercase.

    Returns:
        None
    """
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
        	c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
