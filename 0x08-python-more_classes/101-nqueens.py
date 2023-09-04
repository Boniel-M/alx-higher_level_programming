import sys

def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen at the given row and column position on the chessboard.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index.
        col (int): The column index.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard.

    Raises:
        ValueError: If the provided value of N is not an integer or is less than 4.

    Returns:
        None
    """
    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    if not isinstance(n, int):
        raise ValueError("N must be a number")
    if n < 4:
        raise ValueError("N must be at least 4")

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve(board, 0)

    for solution in solutions:
        for row in solution:
            print(" ".join("Q" if col == 1 else "." for col in row))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError as e:
        print(e)
        sys.exit(1)
