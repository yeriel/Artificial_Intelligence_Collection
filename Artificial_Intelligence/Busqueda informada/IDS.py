def dls(graph, start, goal, depth):
    if start == goal:
        return True

    if depth == 0:
        return False

    for neighbor in graph[start]:
        if dls(graph, neighbor, goal, depth - 1):
            return True

    return False

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):
        if dls(graph, start, goal, depth):
            return True

    return False

graph = {
    'A': ['B', 'C', "D"],
    'B': ['E', "F"],
    'C': ['G', "I"],
    'D': ["I"],
    'E': [],
    "F": [],
    'G': [],
    "I": []
}

start = 'A'
goal = 'G'
max_depth = 4

print(ids(graph, start, goal, max_depth))
# output -> true
'''La salida de este código sería True, lo que indica 
que hay una ruta desde el nodo de inicio 'A' hasta el 
nodo objetivo 'G' '''