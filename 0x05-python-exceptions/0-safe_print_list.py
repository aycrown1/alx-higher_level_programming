#!/usr/bin/python3

"""
Module: safe_print_list
Description:
This module contains a function to safely print elements from a list.
"""


def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first 'x' elements from 'my_list'.

    Args:
        my_list (list, optional):
    The list to print elements from. Defaults to an empty list.
        x (int, optional):
    The number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
