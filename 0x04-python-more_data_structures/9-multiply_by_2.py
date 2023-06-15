#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with all values multiplied by 2.
    """
    multiplied_dictionary = {}
    for key, value in a_dictionary.items():
        multiplied_dictionary[key] = value * 2

    return multiplied_dictionary
