from collections import deque
    
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            stack.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

    return visited

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
print(dfs(graph, start))
# output -> {'I', 'F', 'E', 'G', 'A', 'B', 'D', 'C'}