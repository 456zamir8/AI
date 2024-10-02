import heapq

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state, goal_state):
    distance = 0
    size = len(state)
    for i in range(size):
        for j in range(size):
            value = state[i][j]
            if value != 0:  # Ignore the empty tile
                target_x, target_y = divmod(goal_state.index(value), size)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# Function to generate the goal state for an NxN puzzle
def create_goal_state(size):
    return [[(i * size + j + 1) % (size * size) for j in range(size)] for i in range(size)]

# Function to generate possible moves (successors)
def get_successors(state):
    size = len(state)
    successors = []
    
    # Find the empty tile (0)
    empty_x, empty_y = [(i, j) for i in range(size) for j in range(size) if state[i][j] == 0][0]
    
    # Define the possible moves (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for move in moves:
        new_x, new_y = empty_x + move[0], empty_y + move[1]
        if 0 <= new_x < size and 0 <= new_y < size:
            # Swap the empty tile with the adjacent tile
            new_state = [row[:] for row in state]
            new_state[empty_x][empty_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[empty_x][empty_y]
            successors.append(new_state)
    
    return successors

# A* search algorithm to solve the puzzle
def astar(initial_state, goal_state):
    size = len(initial_state)
    # Flatten the goal state to compare easily with flat state
    goal_flat = sum(goal_state, [])
    
    # Priority queue for A* (cost, state, path)
    heap = []
    heapq.heappush(heap, (0, initial_state, []))
    
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))
    
    while heap:
        cost, current_state, path = heapq.heappop(heap)
        
        # If the goal state is reached, return the path
        if sum(current_state, []) == goal_flat:
            return path + [current_state]
        
        # Generate successors
        for successor in get_successors(current_state):
            successor_tuple = tuple(map(tuple, successor))
            if successor_tuple not in visited:
                new_cost = cost + 1 + manhattan_distance(successor, goal_flat)
                heapq.heappush(heap, (new_cost, successor, path + [current_state]))
                visited.add(successor_tuple)
    
    return None

# Function to print the solution path
def print_solution(solution):
    if solution:
        print("Solution found:")
        for step in solution:
            for row in step:
                print(row)
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    # Initial state of the puzzle
    initial_state = [[1, 2, 3],
                     [4, 0, 5],
                     [7, 8, 6]]  # Example initial state for 3x3 puzzle (8-puzzle)
    
    goal_state = create_goal_state(3)  # Goal state for 3x3 puzzle
    
    # Solve the puzzle using A* search algorithm
    solution = astar(initial_state, goal_state)
    
    # Print the solution path
    print_solution(solution)
