#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a specific position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the column for any queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem and print every possible solution.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)

def solve(board, row):
    """
    Recursively find all solutions to the N-Queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to place a queen.

    Returns:
        None
    """
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    """
    Print a single solution of the N-Queens problem.

    Args:
        board (list): The board representing a solution.

    Returns:
        None
    """
    solution = []
    for row in board:
        for col in range(len(row)):
            if row[col] == 1:
                solution.append([col, row.index(1)])
    print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
