#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        None
    """
    keys = sorted(a_dictionary.keys())
    for key in keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
