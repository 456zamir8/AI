# storing g(n) values
dict_gn = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Oradea': 71, 'Arad': 75},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101},
}

# storing heuristics values 
dict_hn = {
    'Arad': 366,
    'Zerind': 374,
    'Timisoara': 329,
    'Sibiu': 253,
    'Oradea': 380,
    'Lugoj': 244,
    'Fagaras': 176,
    'Rimnicu Vilcea': 193,
    'Mehadia': 241,
    'Pitesti': 100,
    'Bucharest': 0
}
