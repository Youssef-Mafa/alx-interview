#!/usr/bin/python3
"""
The N queens puzzle: placing N non-attacking queens on an N×N chessboard.
"""

import sys


def solveNQueens(N):
    """Solve the N Queens problem using backtracking."""
    solutions = []
    col = set()
    pos_diag = set() 
    neg_diag = set() 

    def backtrack(row, current_solution):
        """Recursively place queens."""
        if row == N:
            solutions.append(current_solution[:])
            return
        for c in range(N):
            if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(row + c)
            neg_diag.add(row - c)
            current_solution.append([row, c])
            backtrack(row + 1, current_solution)
            # Backtrack
            col.remove(c)
            pos_diag.remove(row + c)
            neg_diag.remove(row - c)
            current_solution.pop()

    backtrack(0, [])
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solveNQueens(N)
    for solution in solutions:
        print(solution)
