def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list, considering each integer only once.

    Args:
        my_list (list): The input list of integers.

    Returns:
        int: The sum of all unique integers in the list.
    """
    unique_set = set()
    for num in my_list:
        unique_set.add(num)
    return sum(unique_set)
