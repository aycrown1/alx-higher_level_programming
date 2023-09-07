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
          __size(int): a private instance attribute
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square, Defaults to 0.

        Raises:
             TypeError: If size is not an integer.
             ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
           int: The area of the square.
        """
        return self.__size * self.__size
