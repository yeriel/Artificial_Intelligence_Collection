# Computación Evolutiva

## ¿Que es la Computación Evolutiva?

La Computación Evolutiva es una rama de la inteligencia artificial que se inspira en los procesos evolutivos de la biología, para desarrollar algoritmos y técnicas que permiten resolver problemas complejos de optimización, búsqueda y aprendizaje.

La idea principal detrás de la Computación Evolutiva es la de simular procesos de selección natural, reproducción y mutación para generar soluciones cada vez mejores a un problema dado. En la práctica, esto se traduce en el uso de algoritmos genéticos, estrategias evolutivas, programación evolutiva, entre otros, para buscar soluciones óptimas en un espacio de búsqueda determinado.

Estos algoritmos generan una población inicial de posibles soluciones, y a través de procesos de selección y reproducción, se van creando nuevas soluciones que son sometidas a pruebas de calidad. Aquellas soluciones que resultan más aptas son seleccionadas para reproducirse y generar nuevas soluciones, mientras que las menos aptas son eliminadas. Con el tiempo, el algoritmo encuentra soluciones cada vez mejores, gracias a la aplicación de operadores genéticos como la mutación, la recombinación y la selección natural.

La Computación Evolutiva se utiliza en una amplia variedad de aplicaciones, como la optimización de procesos industriales, el diseño de circuitos eléctricos y electrónicos, la planificación de rutas de transporte, el diseño de redes neuronales artificiales, entre otros.

## Tipos de computación evolutiva
- **Algoritmos genéticos (AG):** Los algoritmos genéticos son una técnica de optimización basada en la evolución biológica, que utiliza operadores genéticos como la selección, la mutación y la recombinación para generar nuevas soluciones a un problema de optimización.

- **Computación artificial de sistemas inmunes (AIS):** La computación artificial de sistemas inmunes se basa en el estudio del sistema inmunológico natural, y tiene como objetivo desarrollar algoritmos de optimización y clasificación inspirados en la inmunología. Los algoritmos AIS utilizan modelos matemáticos para simular el comportamiento de las células del sistema inmunológico, como los linfocitos, para resolver problemas de optimización, detección de patrones y reconocimiento de señales.

- **Sistemas complejos adaptativos (CAS):** Los sistemas complejos adaptativos son sistemas compuestos por múltiples agentes que interactúan entre sí y con su entorno, y que pueden auto-organizarse y adaptarse a cambios en su entorno. Los CAS se utilizan para modelar una amplia variedad de fenómenos complejos, como el comportamiento de los mercados financieros, el tráfico vehicular, la propagación de enfermedades, entre otros.

- **Sistemas dinámicos evolutivos (EDS):** Los sistemas dinámicos evolutivos son sistemas que cambian y evolucionan con el tiempo. Los EDS se utilizan para modelar fenómenos que cambian a lo largo del tiempo, como la evolución biológica, el cambio climático, la propagación de información en redes sociales, entre otros. Los algoritmos EDS utilizan modelos matemáticos para simular la evolución de los sistemas dinámicos y permiten predecir su comportamiento futuro.

## Algoritmos Genéticos

Los algoritmos genéticos (AG) son una técnica de computación evolutiva que se basa en la evolución biológica para resolver problemas de optimización y búsqueda en diferentes campos. Los AG utilizan una población de soluciones candidatas para un problema dado, y luego aplican operadores genéticos como la selección, la mutación y la recombinación para generar nuevas soluciones candidatas que sean mejores que las anteriores.

Los AG siguen un proceso evolutivo iterativo que consta de los siguientes pasos:

- **Inicialización:** se crea una población inicial de soluciones candidatas aleatorias para el problema dado.

- **Evaluación de aptitud:** se evalúa la aptitud de cada solución candidata en la población utilizando una función de aptitud, que mide qué tan bien se desempeña cada solución candidata en el problema dado.

- **Selección:** se seleccionan las soluciones candidatas con mejor aptitud para la reproducción, basándose en un criterio de selección como la ruleta de selección o el torneo de selección.

- **Operadores genéticos:** se aplican los operadores genéticos de mutación y recombinación a las soluciones candidatas seleccionadas para generar nuevas soluciones candidatas.

- **Evaluación de aptitud:** se evalúa la aptitud de las nuevas soluciones candidatas generadas.

- **Reemplazo:** se reemplaza la población actual por la población de nuevas soluciones candidatas generadas, conservando las soluciones de mejor aptitud.

- **Convergencia:** el proceso se repite hasta que se alcance un criterio de convergencia, como una solución satisfactoria o un número máximo de iteraciones.

### Función de Fitness

La función de aptitud o función de fitness en la computación evolutiva es una medida que se utiliza para evaluar qué tan bien se desempeña una solución candidata en el problema que se está intentando resolver

### Genoma y Cromosoma

un genoma es una representación de una solución candidata a un problema en forma de una cadena de genes. Un genoma se compone de uno o más cromosomas, cada uno de los cuales representa una solución candidata.

Un cromosoma es una estructura que contiene un conjunto de genes. Cada gen representa una parte de la solución candidata. Por ejemplo, si la solución candidata es un vector de números reales que resuelve un problema de optimización, entonces cada gen del cromosoma podría representar un número real en el vector. En un problema de clasificación, cada gen podría representar una característica o un atributo de los datos.

Los cromosomas en un algoritmo genético están sujetos a operaciones genéticas, como el crossover y la mutación, que se utilizan para generar nuevas soluciones candidatas a partir de soluciones existentes en la población. Estas operaciones alteran los cromosomas para crear nuevas soluciones candidatas que pueden ser evaluadas utilizando una función de aptitud para determinar qué tan bien resuelven el problema en cuestión.

### ¿Como diseñar un buen genoma?

Para diseñar un genoma para un algoritmo genético, es necesario considerar la naturaleza del problema que se está intentando resolver. El objetivo es diseñar una representación de la solución candidata que permita al algoritmo explorar y explotar el espacio de búsqueda de manera efectiva.

Aquí hay algunos pasos generales para diseñar un genoma para un algoritmo genético:

- **Identificar los componentes de la solución:** identificar los componentes necesarios para construir la solución candidata. Por ejemplo, si se trata de un problema de optimización de funciones, los componentes podrían ser valores de parámetros.

- **Elegir la representación de los componentes:** elegir la representación de los componentes que se utilizará en el genoma. Por ejemplo, si los componentes son valores de parámetros reales, se podría utilizar una representación binaria o real para el genoma.

- **Definir la longitud del genoma:** determinar la longitud del genoma, que se refiere a la cantidad de genes en la cadena del genoma. La longitud del genoma puede ser fija o variable dependiendo del problema.

- **Definir los operadores genéticos:** definir los operadores genéticos que se utilizarán para modificar los genomas. Los operadores genéticos incluyen la mutación y el crossover, y se utilizan para generar nuevas soluciones candidatas a partir de soluciones existentes en la población.

- **Validar el genoma:** validar el genoma para asegurarse de que es capaz de representar todas las soluciones posibles al problema y que permite al algoritmo explorar y explotar el espacio de búsqueda de manera efectiva

### Mutaciones y Crossover

Las mutaciones y el crossover son operadores genéticos utilizados en los algoritmos genéticos y otros métodos de computación evolutiva para generar nuevas soluciones candidatas a partir de soluciones existentes en la población.

La mutación es un operador genético que introduce cambios aleatorios en una solución candidata. En un algoritmo genético, la mutación se utiliza para explorar nuevas regiones del espacio de búsqueda y evitar que el algoritmo se quede atascado en óptimos locales. Por ejemplo, si una solución candidata representa un cromosoma de un problema de optimización, la mutación podría cambiar uno o más genes aleatoriamente en la solución candidata para crear una nueva solución.

El crossover o recombinación es otro operador genético que combina dos soluciones candidatas seleccionadas para generar una nueva solución candidata. El crossover se utiliza para explorar y explotar regiones del espacio de búsqueda de una manera más eficiente que la mutación. En un algoritmo genético, el crossover se realiza seleccionando aleatoriamente dos soluciones candidatas, intercambiando partes de ellas y creando dos nuevas soluciones candidatas.

La elección de los operadores genéticos adecuados es importante para el éxito de un algoritmo genético, ya que influyen en la capacidad del algoritmo para explorar y explotar el espacio de búsqueda. Tanto la mutación como el crossover tienen sus ventajas y desventajas, y su selección depende del problema específico que se está intentando resolver. En general, la mutación se utiliza para explorar regiones del espacio de búsqueda que pueden no ser accesibles a través del crossover, mientras que el crossover se utiliza para combinar soluciones prometedoras y mejorar el rendimiento del algoritmo.

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
