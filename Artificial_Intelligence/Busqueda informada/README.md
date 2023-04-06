# Búsqueda No Informada

## ¿Que es la búsqueda no informada?
La búsqueda no informada es un método de búsqueda en inteligencia artificial que se basa en recorrer sistemáticamente un espacio de soluciones sin utilizar información adicional, más allá de la información proporcionada por el problema en sí mismo. En otras palabras, la búsqueda no informada utiliza únicamente la información contenida en el estado actual del problema y en las reglas que definen cómo se pueden transitar de un estado a otro, sin tener en cuenta ninguna información adicional sobre el problema.

Los algoritmos de búsqueda no informada más comunes son la búsqueda en profundidad (DFS), la búsqueda en anchura (BFS), la búsqueda en profundidad limitada (DLS), y la búsqueda de profundidad iterativa (IDS). Estos algoritmos son útiles para problemas en los que no hay información adicional disponible, como en el caso de juegos como el ajedrez, en los que las reglas y el estado actual del tablero son los únicos datos disponibles para el programa de la IA que juega.

Sin embargo, la búsqueda no informada también puede ser limitada en su capacidad para encontrar soluciones óptimas, ya que puede requerir la exploración de una gran cantidad de estados y rutas para encontrar la solución correcta. Por lo tanto, en problemas más complejos, se pueden utilizar métodos de búsqueda informada, que utilizan información adicional para mejorar la eficiencia de la búsqueda.

## En anchura (BFS)

La estrategia de BFS comienza explorando todos los nodos vecinos del nodo de inicio en un nivel determinado, antes de pasar al siguiente nivel. De esta manera, el algoritmo se asegura de visitar todos los nodos de un nivel antes de avanzar al siguiente nivel.

En términos simples, BFS recorre el árbol de forma horizontal, visitando primero todos los nodos a la misma profundidad antes de pasar a los siguientes niveles. El algoritmo se puede implementar utilizando una cola, donde se agrega el nodo inicial y se explora cada uno de sus vecinos en orden, y luego se agregan los vecinos de los vecinos en la cola.

BFS es útil para encontrar la solución más corta o la ruta más corta entre dos nodos, ya que el algoritmo encuentra la solución más cercana a la raíz antes de avanzar a los siguientes niveles. También es utilizado en la creación de laberintos, en el procesamiento de imágenes, en la detección de ciclos y en muchos otros problemas de optimización y búsqueda de caminos.

## En profundidad (DFS)

La estrategia de DFS comienza en el nodo inicial y explora todos los nodos vecinos en profundidad antes de retroceder y explorar los nodos que no se han visitado todavía. En otras palabras, el algoritmo avanza lo más profundo posible en el árbol antes de retroceder y continuar explorando otros caminos.

DFS se puede implementar utilizando una pila (LIFO), donde se agrega el nodo inicial y se explora cada uno de sus vecinos en profundidad. Si se encuentra un nodo sin vecinos sin visitar, se retrocede y se continúa explorando otros caminos.

DFS es útil para la búsqueda de soluciones en árboles o grafos, para la detección de ciclos en grafos dirigidos o no dirigidos y para el análisis de laberintos. A diferencia de BFS, DFS no garantiza encontrar la solución más corta o la ruta más corta entre dos nodos, pero es más eficiente en términos de memoria ya que utiliza menos espacio de almacenamiento que BFS.

![BFS and DFS](https://www.freelancinggig.com/blog/wp-content/uploads/2019/02/BFS-and-DFS-Algorithms.png)

## En profundidad limitada (DLS)

La estrategia de DLS es similar a la de DFS, pero con la diferencia de que se establece un límite de profundidad, es decir, se establece un nivel máximo hasta donde se permitirá la exploración antes de retroceder. De esta manera, DLS evita que el algoritmo se quede atrapado en un ciclo infinito o en un camino que no lleva a la solución.

DLS se puede implementar utilizando una pila (LIFO), donde se agrega el nodo inicial y se explora cada uno de sus vecinos en profundidad hasta que se alcance el límite de profundidad establecido. Si se encuentra un nodo sin vecinos sin visitar y se ha alcanzado el límite de profundidad, se retrocede y se continúa explorando otros caminos.

DLS es útil en situaciones donde DFS puede quedar atrapado en un ciclo infinito o en un camino que no lleva a la solución. Sin embargo, la profundidad máxima debe ser elegida cuidadosamente para evitar descartar soluciones posibles que están más profundas en el árbol. Si se elige una profundidad demasiado pequeña, es posible que se pierda la solución óptima.

## En profundidad iterativa (IDS)

IDS significa "Búsqueda iterativa en profundidad" (en inglés, Iterative Deepening Search) y es un algoritmo de búsqueda no informada utilizado en inteligencia artificial y ciencias de la computación para recorrer sistemáticamente todos los nodos o estados de un grafo o árbol con una profundidad máxima indeterminada.

La estrategia de IDS es similar a la de DLS, pero en lugar de establecer un límite de profundidad fijo, el algoritmo comienza con una profundidad limitada de 1 y va aumentando la profundidad límite en cada iteración hasta encontrar la solución o hasta alcanzar una profundidad máxima predefinida.

IDS se puede implementar utilizando DLS con una profundidad máxima creciente en cada iteración. En la primera iteración, la profundidad límite es 1, en la segunda es 2, en la tercera es 3 y así sucesivamente hasta que se encuentra la solución o se alcanza la profundidad máxima predefinida.

IDS combina la eficiencia en memoria de DFS con la garantía de completitud y optimidad de BFS, ya que explora primero las soluciones más cercanas a la raíz antes de avanzar a las soluciones más profundas. IDS es especialmente útil cuando se desconoce la profundidad máxima necesaria para alcanzar la solución y cuando el espacio de búsqueda es demasiado grande para almacenar todos los estados posibles.

# Búsqueda Informada

## ¿Que es la búsqueda informada?

La búsqueda informada es un tipo de búsqueda utilizada en inteligencia artificial y ciencias de la computación que utiliza información específica del problema para guiar el proceso de búsqueda hacia la solución deseada de manera más eficiente.

La búsqueda informada se basa en la utilización de una función heurística que estima el costo o la distancia desde un estado o nodo en el espacio de búsqueda hasta el estado objetivo. Esta información heurística se utiliza para guiar la exploración del espacio de búsqueda hacia las soluciones más prometedoras, es decir, aquellas que se espera que estén más cerca de la solución.

Los algoritmos de búsqueda informada más comunes son A* (A-estrella), IDA* (Iterative Deepening A*), y GBFS (Greedy Best-First Search). Estos algoritmos utilizan la información heurística para evaluar y comparar la prometedora de los nodos en el espacio de búsqueda y elegir el próximo nodo a explorar en consecuencia.

La búsqueda informada es útil en problemas donde se dispone de información específica sobre el problema, como el costo de cada acción, la distancia entre los estados, el conocimiento de un objetivo a alcanzar, entre otros. La utilización de información específica del problema permite reducir el espacio de búsqueda y encontrar una solución más eficiente en tiempo y memoria.

## Costo uniforme (UCS)

El algoritmo UCS explora sistemáticamente los nodos en orden creciente de costo, es decir, los nodos con el menor costo acumulado hasta el momento. El costo acumulado de un nodo se define como la suma de los costos de todas las aristas desde el nodo inicial hasta el nodo actual.

UCS utiliza una cola de prioridad para mantener los nodos en orden creciente de costo acumulado y explorar primero los nodos con el menor costo acumulado. Si dos o más nodos tienen el mismo costo acumulado, el algoritmo elige uno de ellos de manera arbitraria.

UCS es completo y óptimo, es decir, siempre encuentra una solución si existe y siempre encuentra la solución de menor costo. Sin embargo, puede ser computacionalmente costoso en grafos o árboles muy grandes o con muchos nodos, ya que debe explorar todos los nodos y aristas para encontrar la solución de menor costo.

## A-star (A*)
A* es una extensión de UCS (Búsqueda de Costo Uniforme) y combina la búsqueda de costo uniforme con una función heurística.

La función heurística de A* se utiliza para estimar el costo del camino restante desde el nodo actual hasta el nodo objetivo. Esta información heurística se combina con el costo acumulado del camino hasta el nodo actual para determinar la siguiente expansión.

A* utiliza una cola de prioridad para almacenar los nodos a explorar, donde el costo de cada nodo se calcula sumando el costo del camino desde el inicio hasta el nodo actual y la estimación heurística del costo restante hasta el objetivo. A* selecciona el siguiente nodo para explorar de la cola de prioridad en función del costo total esperado más bajo.

### ¿A* es optimo ?
A* es óptimo cuando se cumplen dos condiciones:

- La heurística utilizada en A* debe ser **admisible**, lo que significa que nunca sobreestima el costo del camino restante desde el nodo actual hasta el nodo objetivo. Esto garantiza que A* siempre explore primero los nodos más prometedores y evita que el algoritmo se desvíe en la búsqueda de caminos subóptimos.

- El grafo o árbol ponderado en el que se está aplicando A* debe cumplir la propiedad de **consistencia** o **monotonicidad** de la heurística. La propiedad de consistencia significa que la estimación heurística de la distancia desde el nodo actual hasta el nodo objetivo, más el costo de la arista que lleva al siguiente nodo, nunca puede ser menor que la estimación heurística del costo total desde el nodo actual hasta el objetivo.

Si se cumplen ambas condiciones, entonces A* siempre encontrará la solución de menor costo posible. Sin embargo, si la heurística no es admisible o si el grafo no cumple la propiedad de consistencia, entonces A* no necesariamente encontrará la solución de menor costo. En este caso, se pueden utilizar otras variantes de A* o algoritmos de búsqueda más complejos para garantizar la optimización.

## Iterative Deepening A* (IDA*)

IDA* significa "Búsqueda iterativa de A* (en inglés, Iterative Deepening A*)" y es un algoritmo de búsqueda informada utilizado para encontrar el camino más corto o de menor costo entre dos nodos o estados en un grafo o árbol ponderado. IDA* es una variante de A* que no requiere el uso de una cola de prioridad.

IDA* utiliza una función heurística para estimar el costo restante del camino desde el nodo actual hasta el nodo objetivo. En cada iteración, IDA* se expande desde el nodo inicial hasta un cierto límite de profundidad, determinado por la función de costo acumulado más la estimación heurística. Si el nodo objetivo no se encuentra en esa profundidad, se incrementa el límite y se repite el proceso.

Sin embargo, IDA* puede ser más lento que A* en algunos casos, ya que puede expandir nodos múltiples veces a diferentes profundidades. Además, la función heurística utilizada en IDA* debe ser consistente para garantizar la optimización.

## Greedy & GBFS

Greedy (o búsqueda voraz) es un algoritmo de búsqueda heurística utilizado en inteligencia artificial y ciencias de la computación para encontrar una solución rápida, pero no necesariamente óptima, a un problema de optimización. El enfoque de búsqueda voraz consiste en elegir siempre la opción más prometedora en cada etapa de la búsqueda, sin preocuparse por el futuro.

En un algoritmo de búsqueda voraz, se utiliza una función heurística para evaluar cada estado o nodo y se selecciona el estado o nodo con el valor más alto de la función heurística. Este proceso se repite hasta que se alcanza una solución satisfactoria.

A diferencia de los algoritmos de búsqueda informada como A*, que utilizan tanto la información de costo acumulado como la heurística para tomar decisiones, los algoritmos de búsqueda voraz solo consideran la heurística. Esto puede llevar a soluciones subóptimas, ya que la búsqueda puede quedarse atrapada en un camino que parezca prometedor pero no conduzca a la solución óptima.

GBFS significa Búsqueda de mejoría guiada por heurística (en inglés, Greedy Best-First Search).
En GBFS, se utiliza una función heurística para evaluar la distancia desde el nodo actual hasta el nodo objetivo. A diferencia de A*, que utiliza tanto la información del costo acumulado como la heurística para tomar decisiones, GBFS utiliza solo la heurística para elegir el próximo nodo a expandir.

En cada iteración, GBFS expande el nodo con la menor estimación heurística de la distancia al objetivo. Esto significa que GBFS siempre se mueve en la dirección del objetivo, lo que lo convierte en un algoritmo muy eficiente. Sin embargo, GBFS no es completo ni óptimo, ya que puede quedarse atrapado en un camino que parezca prometedor pero que no conduzca a la solución óptima.