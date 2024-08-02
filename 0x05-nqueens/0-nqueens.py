#!/usr/bin/python3
"""Solving the N queens problem"""
import sys


def print_board(board, n):
    """Print the board"""
    base_case = []

    for x in range(n):
        for y in range(n):
            if y == board[x]:
                b.append([x, y])
    print(base_case)


def safe_position(board, x, y, z):
    """safe_position to check if a position is safe"""
    return board[x] in (y, y - x + z, x - z + y)


def determine_positions(board, row, n):
    """determine_positions to determine the positions"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                determine_positions(board, row + 1, n)


def create_board(size):
    """create_board to create the board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
determine_positions(board, row, int(n))