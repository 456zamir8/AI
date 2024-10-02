import random

# Define the objective function to maximize
def objective_function(x):
    return -(x**2) + 10  # Example: a simple quadratic function with a maximum at x = 0

# Hill Climbing function
def hill_climbing(start, step_size, max_iterations):
    current_solution = start
    current_value = objective_function(current_solution)

    for i in range(max_iterations):
        # Generate a neighboring solution by making a small random change
        neighbor = current_solution + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor)

        # If the neighbor solution is better, move to it
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value
            print(f"Iteration {i+1}: Found a better solution at x = {current_solution} with value = {current_value}")

        else:
            print(f"Iteration {i+1}: No improvement found. Stopping.")
            break

    return current_solution, current_value

# Driver code to test the Hill Climbing algorithm
def solve_hill_climbing():
    print("****HILL CLIMBLING PROBLEM****")
    start = float(input("Enter the starting point: ")) # put any number eg 2
    step_size = float(input("Enter the step size: ")) # put any floating number eg 0.1
    max_iterations = int(input("Enter the maximum number of iterations: ")) # enter the size of iterztion eg 100

    best_solution, best_value = hill_climbing(start, step_size, max_iterations)
    print(f"\nBest solution found: x = {best_solution}, value = {best_value}")

solve_hill_climbing()

