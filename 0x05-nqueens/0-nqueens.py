#!/usr/bin/python3
"""
N-Queens Puzzle Solution
Solves for N non-attacking queens in an NxN chessboard.
"""
import sys

def queens(N, row=0, col_set=set(), pos_diag_set=set(), neg_diag_set=set()):

    if row == N:
        yield [[r, c] for r, c in enumerate(col_set)]
    else:
        for col in range(N):
            pos_diag = row + col
            neg_diag = row - col
            if col not in col_set and pos_diag not in pos_diag_set and neg_diag not in neg_diag_set:
                yield from queens(N, row + 1, col_set | {col}, pos_diag_set | {pos_diag}, neg_diag_set | {neg_diag})

def main():

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

    for solution in queens(N):
        print(solution)

if __name__ == "__main__":
    main()
