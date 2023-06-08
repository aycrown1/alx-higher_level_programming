#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """
    This script prints the number of arguments passed to it
    and the list of those arguments.

    Usage: ./2-args.py arg1 arg2 ...

    Output format:
    Number of argument(s): <num_args>. (if no arguments)
    Number of argument(s): <num_args>: (if at least one argument)
    <position>: <arg_value>
    ...
    """
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
