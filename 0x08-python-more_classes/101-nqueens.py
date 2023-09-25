#!/usr/bin/python3
"""
Usage: nqueens N
    If the user called the program with the wrong number of arguments,
       print Usage: nqueens N, followed by a new line,
            and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number,
        followed by a new line, and exit with the status 1
    If N is smaller than 4, print N must be at least 4,
        followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
    Format:
       julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
       [[0, 1], [1, 3], [2, 0], [3, 2]]
       [[0, 2], [1, 0], [2, 3], [3, 1]]
       julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
       [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
       [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
       [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
       [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
       julien@ubuntu:~/0x08. N Queens$

You don’t have to print the solutions in a specific order
"""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]
            without attacking other queens"""
    N = len(board)

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """Print a solution in the specified format"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def solve_nqueens(N):
    """Solve the N-Queens problem and print solutions"""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []

    def solve(row):
        if row == N:
            solutions.append([row[:] for row in board])  # Found a solution
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)

    for solution in solutions:
        print_solution(solution)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
