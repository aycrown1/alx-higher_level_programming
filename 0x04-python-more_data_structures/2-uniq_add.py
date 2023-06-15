#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list, considering each integer only once.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    integer = 0
    for element in set(my_list):
        integer += element
    return integer
