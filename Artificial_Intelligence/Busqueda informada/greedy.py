import math

# Definir la matriz de adyacencia
graph = {
    'A': {'B': 2, 'C': 4, 'D': 7},
    'B': {'E': 3, 'F': 5},
    'C': {'G': 6},
    'D': {'H': 9, 'I': 10},
    'E': {'I': 8},
    'F': {'I': 6},
    'G': {'I': 7},
    'H': {'I': 4},
    'I': {}
}

# Definir las coordenadas cartesianas de cada nodo
coordinates = {
    'A': (0, 0),
    'B': (1, 1),
    'C': (1, -1),
    'D': (2, 0),
    'E': (2, 2),
    'F': (2, -2),
    'G': (3, -1),
    'H': (3, 1),
    'I': (4, 0)
}

def distance_euclidean(a, b):
    x1, y1 = coordinates[a]
    x2, y2 = coordinates[b]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def greedy(start, goal):
    path = [start]
    cost = 0
    
    while path[-1] != goal:
        # Obtener el último nodo en el camino
        current_node = path[-1]
        
        # Encontrar el nodo vecino más cercano al objetivo
        nearest_neighbor = min(graph[current_node], key=lambda x: distance_euclidean(x, goal))
        
        # Agregar el nodo vecino al camino
        path.append(nearest_neighbor)
        
        # Actualizar el costo total
        cost += graph[current_node][nearest_neighbor]
    
    return path, cost

# Ejecutar la función Greedy con el nodo de inicio A y el nodo objetivo I
path, cost = greedy('A', 'I')

print(" -> ".join(path))
print("Costo total:", cost)
