#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """
    This script prints
     the result of the addition of all command-line arguments.

    Usage: ./3-infinite_add.py arg1 arg2 ...

    Output format:
    <sum_of_arguments>
    """

    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
