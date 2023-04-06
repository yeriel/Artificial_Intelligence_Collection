from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            queue.extend([neighbor for neighbor in graph[vertex] if neighbor not in visited])

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
print(bfs(graph, start))
# output -> {'I', 'F', 'E', 'G', 'B', 'A', 'D', 'C'}