import heapq
import math

def distance_euclidean(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 3, 'E': 3},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 3, 'E': 1},
    'E': {'B': 3, 'D': 1, 'H': 4},
    'F': {'C': 5, 'G': 1},
    'G': {'F': 1, 'I': 2},
    'H': {'E': 4, 'I': 3},
    'I': {'G': 2, 'H': 3}
}

# Coordenadas de los nodos para la heurística
coordinates = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (1, -1),
    'D': (3, 2),
    'E': (3, 0),
    'F': (2, -3),
    'G': (3, -4),
    'H': (6, 1),
    'I': (6, -2)
}

heuristic = {node: distance_euclidean(coord, coordinates['I']) for node, coord in coordinates.items()}
start, goal = 'A', 'I'
path = a_star(graph, start, goal, heuristic)
print(f"Camino desde {start} hasta {goal}: {path}")