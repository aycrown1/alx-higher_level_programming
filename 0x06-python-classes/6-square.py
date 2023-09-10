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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square, Defaults to 0.
            position (tuple of 2): The position of the new square.
        Raise:
            TypeError: If value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """
        retrive the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the current positon
        Attribute:
            value (int): the new positon of the square
        Raise:
            TypeError: If value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        retrive the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the current positon
        Attribute:
            value (int): the new positon of the square
        Raise:
            TypeError: If value is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        retrive the current position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the current positon
        Attribute:
            value (int): the new positon of the square
        Raise:
           TypeError: If value is not a tuple and element not an int
        """
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

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

    def my_print(self):
        """
         prints in stdout the square with the character #:
             if size is equal to 0, print an empty line
        """
        if isinstance(self.__size, int) is not True:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        if self.__size == 0:
            print("")
        else:
            print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)
