#!/usr/bin/python3
"""
This module defines the Square class.
Classes:
    Square: Represents a square shape.
"""


class Square:
    """
    Class: Square that defines the atrributes of a square shape
    Atrribute:
          __size(int): a private inatance attribute
    """
    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
