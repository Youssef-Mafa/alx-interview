#!/usr/bin/python3
""" N-Queens Puzzle Solver """
import sys

def validate_input():
    """Validate command-line input"""
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
    return N

def solveNQueens(N):
    """Solve the N-Queens problem"""
    col, pos_diag, neg_diag = set(), set(), set()  # use sets for efficiency
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append([[i, c] for i, c in enumerate(col)])
            return
        for c in range(N):
            if c in col or (row + c) in pos_diag or (row - c) in neg_diag:
                continue
            col.add(c)
            pos_diag.add(row + c)
            neg_diag.add(row - c)
            backtrack(row + 1)
            col.remove(c)
            pos_diag.remove(row + c)
            neg_diag.remove(row - c)

    backtrack(0)
    return solutions

def main():
    """Main function"""
    N = validate_input()
    solutions = solveNQueens(N)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
