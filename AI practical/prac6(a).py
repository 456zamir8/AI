# MISSIONARIES AND CANNABIS PROBLEM SOLUTION

from collections import deque

# State: (missionaries_left, cannibals_left, boat_position, missionaries_right, cannibals_right)
# boat_position = 0 means the boat is on the left bank, 1 means the boat is on the right bank

def is_valid(state):
    ml, cl, boat, mr, cr = state
    # Check if any side has more cannibals than missionaries (invalid)
    if ml < 0 or cl < 0 or mr < 0 or cr < 0:
        return False
    if (ml > 0 and ml < cl) or (mr > 0 and mr < cr):
        return False
    return True

def get_successors(state):
    ml, cl, boat, mr, cr = state
    successors = []
    
    if boat == "left":  # Boat on the left bank
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible moves (missionaries, cannibals)
        for m, c in moves:
            new_state = (ml - m, cl - c, "right", mr + m, cr + c)
            if is_valid(new_state):
                successors.append(new_state)
    else:  # Boat on the right bank
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for m, c in moves:
            new_state = (ml + m, cl + c, "left", mr - m, cr - c)
            if is_valid(new_state):
                successors.append(new_state)
    
    return successors

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # Queue of (state, path)
    visited = set()
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [current_state]
        
        for successor in get_successors(current_state):
            if successor not in visited:
                visited.add(successor)
                queue.append((successor, path + [current_state]))
    
    return None

def print_solution(solution):
    if solution:
        print("Solution found:")
        print("missionaries_left, cannibals_left, boat_position, missionaries_right, cannibals_right")
        print("ml,cl,boat,mr,cr")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    initial_state = (3, 3, "left", 0, 0)  # All missionaries and cannibals on the left bank
    goal_state = (0, 0, "right", 3, 3)     # All missionaries and cannibals on the right bank
    solution = bfs(initial_state, goal_state)
    print_solution(solution)
