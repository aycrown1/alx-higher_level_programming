#!/usr/bin/python3
"""
This script imports functions from the file 'calculator_1.py',
performs mathematical operations using the imported functions,
and prints the results.

Variables:
- a: assigned the value 10
- b: assigned the value 5

The results of addition, subtraction, multiplication, and division are printed.
"""

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print('{:d} + {:d} = {:d}'.format(a, b, (add(a, b))))
    print('{:d} - {:d} = {:d}'.format(a, b, (sub(a, b))))
    print('{:d} * {:d} = {:d}'.format(a, b, (mul(a, b))))
    print('{:d} / {:d} = {:d}'.format(a, b, (div(a, b))))
