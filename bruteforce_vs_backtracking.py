from n_queens_backtracking import n_queens
from n_queens_brutforce import brute_force_nqueens
import matplotlib.pyplot as plt

def plot_graph(n_values, backtracking_times, brute_force_times):
    plt.figure(figsize=(10, 6))
    
    plt.plot(n_values, backtracking_times, label='Backtracking', color='red', marker='o')
    plt.plot(n_values, brute_force_times, label='Brute Force', color='blue', marker='o')

    plt.xlabel("Number of Queens (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Time Comparison: Backtracking vs Brute Force")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    n_values = [4, 6, 8] #using no. of queens for comparison
    backtracking_times = []
    brute_force_times = []

    for current_n in n_values:
        backtracking_time = n_queens(current_n)
        backtracking_times.append(backtracking_time)

        brute_force_time = brute_force_nqueens(current_n)
        brute_force_times.append(brute_force_time)
    
    for current_n, backtracking_time, brute_force_time in zip(n_values, backtracking_times, brute_force_times):
        print(f"\nBacktracking Time for n={current_n}: {backtracking_time:.6f} seconds")
        print(f"Brute Force Time for n={current_n}: {brute_force_time:.6f} seconds")

    plot_graph(n_values, backtracking_times, brute_force_times)

if __name__ == "__main__":
    main()
