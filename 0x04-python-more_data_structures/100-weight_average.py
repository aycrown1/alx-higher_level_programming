#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Returns the weighted average of integers in a list of tuples.

    Args:
        my_list (list): The input list of tuples.

    Returns:
        float: The weighted average of integers.
               Returns 0 if the list is empty.
    """
    if not my_list:
        return 0

    sum_product = 0
    total_weight = 0

    for score, weight in my_list:
        sum_product += score * weight
        total_weight += weight

    weighted_average = sum_product / total_weight

    return weighted_average
