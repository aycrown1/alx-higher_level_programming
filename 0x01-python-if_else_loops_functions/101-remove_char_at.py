#!/usr/bin/python3
def remove_char_at(string, n):
    """
    Create a copy of the string,
    removing the character at position n.

    Args:
        string (str): The input string.
        n (int): The position of the character to be removed.

    Returns:
        str: The new string with the character removed.
    """
    if n < 0 or n >= len(string):
        return string

    new_string = ""
    for i in range(len(string)):
        if i != n:
            new_string += string[i]

    return new_string
