# N-Queen problem

def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(board, row, n, solutions):
    # Base case: If all queens are placed, add solution
    if row >= n:
        solution = []
        for r in board:
            solution.append(r[:])  # Copy the board state
        solutions.append(solution)
        return

    # Try placing the queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = 'Q'

            # Recur to place the rest of the queens
            solve_n_queens(board, row + 1, n, solutions)

            # Backtrack if placing queen in board[row][col] doesn't lead to a solution
            board[row][col] = '.'

def print_solutions(solutions, n):
    for index, solution in enumerate(solutions):
        print(f"Solution {index + 1}:")
        for row in solution:
            print(" ".join(row))
        print()

def solve_n_queens_problem():
    print("****N-QUEEN PROBLEM****")
    n = int(input("Enter the value of n for the N-Queens problem: "))
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)

    if solutions:
        print(f"{len(solutions)} solutions found for {n}-Queens problem:")
        print_solutions(solutions, n)
    else:
        print(f"No solution exists for {n}-Queens problem.")

solve_n_queens_problem()