# Búsqueda Local
## ¿Que es la búsqueda local?

La búsqueda local es una técnica de optimización utilizada en inteligencia artificial para resolver problemas de optimización. En la búsqueda local, se comienza con una solución aleatoria y se busca una solución óptima haciendo pequeños cambios iterativos en la solución actual. En cada iteración, se evalúa la calidad de la solución modificada y se decide si se debe aceptar o rechazar la modificación. Este proceso se repite hasta que se encuentra una solución que se considera óptima o hasta que se alcanza un límite de tiempo o de iteraciones.

Existen varios algoritmos de búsqueda local en IA, algunos de los más comunes son:

- **Hill Climbing:** Este algoritmo comienza en un punto aleatorio y luego se mueve hacia la dirección del mayor aumento de la función de evaluación. Continúa haciendo esto hasta que se alcanza un máximo local. A veces, puede quedar atrapado en un máximo local y no llegar al máximo global.

- **Recocido Simulado (Simulated Annealing):** Este algoritmo es similar a Hill Climbing, pero también permite la posibilidad de moverse a un punto peor (aunque con una probabilidad decreciente a lo largo del tiempo). Esto permite escapar de los máximos locales y encontrar soluciones mejores.

- **Búsqueda Tabú (Tabu Search):** Este algoritmo mantiene una lista de soluciones recientes y no permite moverse a soluciones que estén en la lista tabú. Esto ayuda a evitar ciclos y puede llevar a soluciones mejores.

## Hill Climbing
Hill Climbing es una técnica de optimización matemática que pertenece a la familia de la búsqueda local. Es un algoritmo iterativo que comienza con una solución arbitraria a un problema y luego intenta encontrar una solución mejor haciendo un cambio incremental en la solución. Si el cambio produce una solución mejor, se hace otro cambio incremental a la nueva solución, y así sucesivamente hasta que no se pueden encontrar más mejoras.

Hill Climbing encuentra soluciones óptimas para problemas convexos, pero para otros problemas solo encontrará óptimos locales, que no necesariamente son la mejor solución posible (el óptimo global) de todas las soluciones posibles (el espacio de búsqueda). Para intentar evitar quedarse atascado en óptimos locales, se pueden utilizar reinicios, esquemas más complejos basados en iteraciones o en memoria, o modificaciones estocásticas sin memoria.

Aunque hay algoritmos más avanzados que pueden dar mejores resultados, la simplicidad del algoritmo lo hace una opción popular para algoritmos de optimización, y se utiliza ampliamente en inteligencia artificial para llegar a un estado objetivo desde un nodo de partida. Hill Climbing puede producir un mejor resultado que otros algoritmos cuando se dispone de poco tiempo para realizar una búsqueda, como en sistemas en tiempo real. Es un algoritmo "anytime", lo que significa que puede devolver una solución válida incluso si se interrumpe en cualquier momento antes de que termine.

### Pseudo código
```
retorna un estado que es un maximo local

función HILL_CLIMBING(poblema)
    actual <- problema.Inicial
    while True
    vecino <- Valor sucesor mas alto que el actual
    if VALUE(vecino) <= VALUE(actual) then return actual
    actual <- vecino
```
### Tipos de algoritmos de Hill Climbing

**Hill Climbing Simple:** El método más simple de subir una colina se llama Hill Climbing Simple. El objetivo es ascender al pico más alto de la montaña. Aquí, los pasos y movimientos del escalador determinan cómo se mueve. Continúa moviéndose si cree que su próximo paso será mejor que el anterior, o si se queda en la misma posición. Esta búsqueda solo se preocupa por sus acciones previas y subsecuentes.

**Hill Climbing Estocástico:** Los nodos no están todos concentrados en Hill Climbing estocástico. Elige un nodo al azar y luego determina si ampliarlo o buscar uno mejor.

**Hill Climbing de Reinicio Aleatorio:** El enfoque de intentar una y otra vez es la base del algoritmo de reinicio aleatorio. Hasta que no se alcance el objetivo, busca iterativamente el nodo y elige el mejor candidato en cada etapa. Con frecuencia, el éxito se determina por la forma de la colina. Es más fácil llegar allí si no hay muchas crestas, mesetas o máximos locales.

## Simulated Annealing
Simulated Annealing (SA) es una técnica probabilística para aproximar el óptimo global de una función dada en un espacio de búsqueda grande. Se usa comúnmente cuando el espacio de búsqueda es discreto y para problemas donde encontrar un óptimo global aproximado es más importante que encontrar un óptimo local preciso en un tiempo fijo. El nombre del algoritmo proviene del proceso de recocido en metalurgia, que involucra calentar y enfriar un material controladamente para alterar sus propiedades físicas.

En SA, la temperatura disminuye gradualmente, disminuyendo la probabilidad de aceptar soluciones peores, lo que permite una búsqueda más extensa de la solución óptima global. El algoritmo selecciona aleatoriamente una solución cercana a la solución actual, mide su calidad y se mueve hacia ella de acuerdo con las probabilidades dependientes de la temperatura de seleccionar soluciones mejores o peores. SA se usa comúnmente para problemas computacionales difíciles donde los algoritmos exactos fallan.

### Pseudo código
```
retorna un estado que es una solución factible

función SIMULATED_ANNEALING(poblema)
    actual <- problema.Inicial
    for t = 1 to inf do
        T <- encolar(t)
        if T = 0 then return actual
        siguiente <- sucesor aleatorio al actual
        E <- VALUE(actual) - VALUE(siguiente)
        if E > 0 then actual <- siguiente
        else actual <- siguiente solo si e^-(E/T) 
```
## Tabu Search
La búsqueda Tabu es un método de búsqueda heurístico para resolver problemas de optimización combinatoria. Se basa en la idea de utilizar una "lista tabu" para hacer un seguimiento de las soluciones visitadas recientemente y prohibir su re-visita en el futuro cercano. Esto ayuda al algoritmo a evitar quedar atrapado en óptimos locales y explorar una gama más amplia del espacio de búsqueda.

En la búsqueda Tabu, el algoritmo comienza con una solución inicial y genera e evalúa iterativamente soluciones vecinas, seleccionando la mejor como la solución actual. Durante este proceso, el algoritmo mantiene una lista tabu, que almacena las soluciones visitadas recientemente y sus movimientos correspondientes. El algoritmo evita revisitar cualquier solución en la lista tabu, excepto en ciertas condiciones. Esto ayuda al algoritmo a moverse a regiones nuevas e inexploradas del espacio de búsqueda.

El algoritmo de búsqueda Tabu también incluye varios mecanismos para controlar la búsqueda, como estrategias de diversificación para escapar de óptimos locales, estrategias de intensificación para centrarse en regiones prometedoras y criterios de aspiración para permitir la revisión de soluciones tabu que mejoren la mejor solución actual

## Algoritmos Evolutivos
Los algoritmos evolutivos son una clase de algoritmos de optimización y búsqueda inspirados en la evolución biológica y en la teoría de la selección natural. Se basan en el proceso de selección natural para encontrar soluciones óptimas a un problema.

En un algoritmo evolutivo, se crea una población inicial de posibles soluciones al problema. Luego, se aplican operaciones de selección, mutación y cruce a la población para generar una nueva generación de soluciones. Estas operaciones imitan el proceso de selección natural, mutación y reproducción en la biología.

La selección asegura que las soluciones más aptas tengan una mayor probabilidad de ser seleccionadas para reproducirse, mientras que la mutación y el cruce generan nuevas soluciones a partir de soluciones existentes. El proceso de selección, mutación y cruce se repite varias veces para obtener una población de soluciones cada vez mejor adaptadas al problema.

### Pseudo código
```
retorna un individuo

función Genetic_Algorithm(población, fitness)
    repetir 
        pesos <- Weighted_By(población, fitness)
        población2 <- list()
        for i = 1 to Size(población) do
            padre1, padre2 <- Weighted_random_Choices(población, pesos,2)
            hijos <- Reproduce(padre1, padre2)
            if población aleatoria pequeña then 
                hijo <- Mutate(hijos)
                add hijos to población2
            población <- población2
            until que un individuo se el mejor o termine el tiempo
            return el mejor individuo de la población

function Reproduce(padre1, padre2) retorna un individuo
    n <- Length(padre1)
    c <- numero aleatorio 1 y n
    return Append(Substring(padre1,1,c), Substring(padre2,c+1,n))
```
## Algoritmos de Enjambres
Los algoritmos de enjambres, también conocidos como algoritmos de inteligencia de enjambre, son un tipo de algoritmo de optimización que se basa en el comportamiento colectivo de los individuos en una colonia o enjambre para encontrar soluciones a un problema.

Estos algoritmos están inspirados en el comportamiento de los animales en la naturaleza, como las abejas, los pájaros y las hormigas, que trabajan juntos en grupo para lograr objetivos comunes.

En un algoritmo de enjambre, se crea una población de individuos llamados "partículas" que se mueven en un espacio de búsqueda. Cada partícula representa una posible solución al problema y se mueve a través del espacio de búsqueda, siguiendo un conjunto de reglas simples y modificando su posición en función de su propio rendimiento y del rendimiento de las partículas vecinas.

La posición de cada partícula en el espacio de búsqueda es actualizada en función de su propio rendimiento y del rendimiento de las partículas vecinas. Este proceso de actualización se repite varias veces hasta que se encuentra una solución satisfactoria o se alcanza un número máximo de iteraciones.