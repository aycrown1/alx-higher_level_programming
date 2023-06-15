#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key (str): The key to delete.

    Returns:
        dict: The updated dictionary after deleting the key.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
