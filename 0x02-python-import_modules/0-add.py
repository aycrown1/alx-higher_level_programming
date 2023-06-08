#!/usr/bin/python3
"""
This script imports the function 'add' from the file 'add_0.py'
and prints the result of the addition a + b.

a = 1
b = 2

The result is printed in the format:
       '<a value> + <b value> = <add(a, b) value>'
"""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
