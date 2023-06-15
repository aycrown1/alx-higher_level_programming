#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers in a matrix.

    Args:
        matrix (list[list[int]]): The input matrix of integers.

    Returns:
        list[list[int]]: A new matrix with the same size as the input matrix.
        Each value in the new matrix is
        the square of the corresponding value in the input matrix.
        The input matrix remains unmodified.
    """
    # Create a new matrix with the same size as the input matrix
    result = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))

    return result
