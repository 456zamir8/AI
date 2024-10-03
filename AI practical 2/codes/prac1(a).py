import queue as Q
from RMP import dict_gn
# USING BREATH FIRST SEARCH (BFS) ALGORITHM TO SOLVE THE FOLLOWING PROBLEM

start = 'Zerind'
goal = 'Bucharest'

def BFS(start, goal):
    cityq = Q.Queue()  # Queue for BFS traversal
    visited = set()  # Set to store visited cities
    cityq.put(start)  # Start from the initial city
    path = {start: None}  # Dictionary to store the path

    while not cityq.empty():
        city = cityq.get()  # Get the current city
        visited.add(city)

        # Check if we reached the goal
        if city == goal:
            return reconstruct_path(path, start, goal)

        # Add neighbors to the queue
        for neighbor in dict_gn[city].keys():
            if neighbor not in visited and neighbor not in cityq.queue:
                cityq.put(neighbor)
                path[neighbor] = city  # Track the parent city

    return None  # If no path found

# Function to reconstruct the path from start to goal
def reconstruct_path(path, start, goal):
    result = []
    current_city = goal
    while current_city is not None:
        result.append(current_city)
        current_city = path[current_city]
    result.reverse()  # Reverse the path to get it from start to goal
    return " -> ".join(result)

def main():
    result = BFS(start, goal)
    if result:
        print("BFS Traversal from", start, "to", goal, "is:", result)
    else:
        print("No path found from", start, "to", goal)

main()
