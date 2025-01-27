import matplotlib.pyplot as plt
import numpy as np
import time

# check if a queen can be placed at board[row][col]
def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check diagonal (upper left)
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check diagonal (upper right)
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == 1:
            return False
    return True

# Backtracking function to solve N-Queens problem
def solve_nqueens(board, row, n):
    if row == n:
        return True  # All queens are placed successfully
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            print_board(board)  # Display the current board state in terminal
            if solve_nqueens(board, row + 1, n):  # Recursively place queens in next row
                return True
            board[row][col] = 0  # Backtrack if placing the queen leads to no solution

    return False

# print the board state
def print_board(board):
    print("\nCurrent Board State:")
    for row in board:
        print(" ".join(['Q' if col == 1 else '.' for col in row]))
    print("\n")

def visualize_board(board, n):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, n, 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    for i in range(n):
        for j in range(n):
            color = 'white' if (i + j) % 2 == 0 else 'black'
            ax.add_patch(plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black'))
            if board[i][j] == 1:
                ax.text(j + 0.5, i + 0.5, 'Q', ha='center', va='center', fontsize=20, color='red')

    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.show()

def n_queens(n):
    start_time = time.time()
    board = [[0] * n for _ in range(n)]  # Initialize the board with 0s
    if solve_nqueens(board, 0, n):
        end_time = time.time()
        total_time = end_time - start_time
        print("\nSolution Found using Backtracking.")
        visualize_board(board, n)
        return total_time
    else:
        print("\nNo Solution Found")

# n = int(input("Enter the number of queens: "))
# n_queens(n)

