from simpleai.search import SearchProblem, astar
import time
from colorama import init, Fore, Style

init(autoreset = True)

GOAL = input("Enter text u wanna search: ")

class HelloProblem(SearchProblem):

    def __init__(self, initial_state, goal):
        self.GOAL = goal
        super(HelloProblem, self).__init__(initial_state)

    def actions(self, state):
        # Only allow actions if we haven't reached the goal length
        if len(state) < len(GOAL):
            possible_actions = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        else:
            possible_actions = []
        
        return possible_actions

    def result(self, state, action):
        # Create the new state by appending the action (character)
        new_state = state + action
        return new_state

    def is_goal(self, state):
        # Check if the current state matches the goal
        goal_reached = state == GOAL
        return goal_reached

    def heuristic(self, state):
        # Calculate the number of mismatched characters
        wrong = sum(1 for i in range(len(state)) if state[i] != GOAL[i])
        # Calculate the number of missing characters
        missing = len(GOAL) - len(state)
        heuristic_value = wrong + missing
        return heuristic_value

# Initial state is an empty string
problem = HelloProblem("", GOAL)

# Measure the time taken by A* search
start_time = time.time()
result = astar(problem, graph_search=True)
end_time = time.time()

# Print results
print(Fore.GREEN + "\nSearch complete.")
print((Fore.RED + "Result State:"), result.state)
print((Fore.RED +"Path:"), result.path())
print(Fore.RED + f"Time taken: {end_time - start_time:.4f} seconds")
