import random 
GENES_PER_CROMOSOMA = 3

def fitness_func(solution):
    # evalúa la calidad de la solución candidata
    return sum(solution)/len(solution) 

def create_population(population_size):
    population = []
    for i in range(population_size):
        # crea una solución candidata aleatoria
        genome = [random.uniform(0, 1) for _ in range(GENES_PER_CROMOSOMA)]
        population.append(genome)
    return population

def mutate(genome):
    # muta un gen aleatorio en el genoma
    index = random.randint(0, GENES_PER_CROMOSOMA - 1)
    genome[index] = random.uniform(0, 1)

def crossover(parent1, parent2):
    # combina los cromosomas de dos padres para crear un hijo
    child = []
    for i in range(GENES_PER_CROMOSOMA):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

def roulette_selection(population, fitness_values):
    # calcula el valor total de aptitud
    total_fitness = sum(fitness_values)

    # elige un punto aleatorio en la ruleta
    selection_point = random.uniform(0, total_fitness)

    # selecciona un individuo proporcionalmente a su aptitud
    cumulative_fitness = 0
    for i in range(len(population)):
        cumulative_fitness += fitness_values[i]
        if cumulative_fitness >= selection_point:
            return population[i]

def run_ga(population_size, generations):
    population = create_population(population_size)
    for i in range(generations):
        # evalúa la aptitud de la población actual
        fitness_values = [fitness_func(solution) for solution in population]

        # selecciona a los padres utilizando la ruleta
        parent1 = roulette_selection(population, fitness_values)
        parent2 = roulette_selection(population, fitness_values)

        # crea hijos mediante crossover y mutación
        child = crossover(parent1, parent2)
        mutate(child)

        # evalúa la aptitud del hijo
        child_fitness = fitness_func(child)

        # reemplaza al peor sobreviviente con el hijo
        worst_index = fitness_values.index(min(fitness_values))
        if child_fitness > fitness_values[worst_index]:
            population[worst_index] = child

    # devuelve la mejor solución encontrada
    best_index = fitness_values.index(max(fitness_values))
    return population[best_index]

def run_ga(population_size, generations):
    population = create_population(population_size)
    for i in range(generations):
        # evalúa la aptitud de la población actual
        fitness_values = [fitness_func(solution) for solution in population]

        # selecciona a los padres utilizando la ruleta
        parent1 = roulette_selection(population, fitness_values)
        parent2 = roulette_selection(population, fitness_values)

        # crea hijos mediante crossover y mutación
        child = crossover(parent1, parent2)
        mutate(child)

        # evalúa la aptitud del hijo
        child_fitness = fitness_func(child)

        # reemplaza al peor sobreviviente con el hijo
        worst_index = fitness_values.index(min(fitness_values))
        if child_fitness > fitness_values[worst_index]:
            population[worst_index] = child

    # devuelve la mejor solución encontrada
    best_index = fitness_values.index(max(fitness_values))
    return population[best_index]

print(f'La mejor solucion es: {run_ga(10, 5)}')