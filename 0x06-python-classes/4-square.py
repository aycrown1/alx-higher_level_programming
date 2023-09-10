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
        Raise:
            TypeError: If value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        retrives the property of the saquare
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set property size
        Attribute:
            value (int): the new size of the square
        Raise:
            TypeError: If value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.
        Returns:
           int: The area of the square.
        """
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        return self.__size * self.__size
