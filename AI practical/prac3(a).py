import math

# Alpha-Beta Pruning function
def alpha_beta_search(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: If we have reached the leaf node
    if depth == 0 or node_index >= len(values):
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf

        for i in range(2):  # Each node has 2 children
            eval = alpha_beta_search(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)

            # Alpha-Beta pruning
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = math.inf

        for i in range(2):
            eval = alpha_beta_search(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)

            # Alpha-Beta pruning
            if beta <= alpha:
                break
        return min_eval

# Driver code to test the Alpha-Beta search
def solve_alpha_beta():
    print("****ALPHA-BETA PROBLEM****")
    values = [int(x) for x in input("Enter leaf node values (space-separated): ").split()] # enter a set of number eg 2 12 78 78 1 1
    depth = int(input("Enter depth of the game tree: ")) # enter the depth of the tree eg 3
    
    # Start Alpha-Beta search
    result = alpha_beta_search(depth, 0, True, values, -math.inf, math.inf)
    print(f"The optimal value is: {result}\n")

solve_alpha_beta()