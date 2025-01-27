import itertools
import matplotlib.pyplot as plt
import numpy as np
import time

# check if a configuration is valid
def is_valid(board, n):
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                return False  # Same column
            if abs(board[i] - board[j]) == j - i:
                return False  # Same diagonal
    return True

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
            if board[i] == j:
                ax.text(j + 0.5, i + 0.5, 'Q', ha='center', va='center', fontsize=20, color='red')

    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.show()

def brute_force_nqueens(n):
    start_time = time.time()
    # Generate all permutations of column positions for n queens
    columns = list(itertools.permutations(range(n)))
    step = 1  # Step counter to show each configuration
    for board in columns:
        # print each configuration
        print(f"Step {step}:")
        for i in range(n):
            row = ['.' for _ in range(n)]
            row[board[i]] = 'Q'
            print(" ".join(row))
        
        # Check if the current configuration is valid
        if is_valid(board, n):
            end_time = time.time()
            total_time = end_time - start_time
            print("Valid Configuration Found using Brute Force.")
            visualize_board(board, n)
            return total_time
        else:
            print("Invalid Configuration\n")
        
        step += 1

# n = int(input("Enter the number of queens: "))
# brute_force_nqueens(n)