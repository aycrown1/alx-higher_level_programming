#!/usr/bin/python3
"""
module: prints an integer with "{:d}".format()
function:
	safe_print_integer
"""


def safe_print_integer(value):
	"""
	safe_print_integer:
		print the integer and handles exception  if value is an integer
		args:
		 value: value can be any type (integer, string, etc.)
	"""
	try:
		print("{:d}".format(value))
		return True
	except:
		return False
