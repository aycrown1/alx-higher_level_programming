#!/usr/bin/python3
"""
This module prints the first x elements of a list and only integers.
func: safe_print_list_integers
"""

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements of a list and only integers
    args:
    	my_list: a list that contain any type (integer, string, etc.)
    	x: represents the number of elements to access in my_list
    return:  the real number of integers printed.
    """

    index = 0
    for num in range(x):
        index += 1
        try:
            print("{:d}".format(my_list[num]), end='')
        except (ValueError, TypeError):
            index -= 1
    print("")
    return index
