import heapq

def ucs(graph, start, goal):
    heap = [(0, start)]
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return cost

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor))

    return None

graph = {
    'A': {'B': 3, 'C': 2, 'D': 1},
    'B': {'E': 4, 'F': 1},
    'C': {'G': 2, 'I': 3},
    'D': {'I': 1},
    'E': {},
    'F': {},
    'G': {},
    'I': {}
}

start = 'A'
goal = 'G'

print(ucs(graph, start, goal))
#output -> 4 
'''La salida de este código sería 4, 
lo que indica que la ruta de menor costo 
desde el nodo de inicio 'A' hasta el nodo 
objetivo 'G' tiene un costo total de 4'''