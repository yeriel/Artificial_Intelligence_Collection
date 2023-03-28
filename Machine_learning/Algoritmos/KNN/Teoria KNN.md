# K-Nearest Neighbors (KNN)

## Representación del Modelo
La representación del modelo para KNN es el conjunto completo de datos de entrenamiento. Es tan simple como eso. KNN no tiene ningún otro modelo aparte de almacenar el conjunto de datos completo, por lo que no se requiere aprendizaje. 

Implementaciones eficientes pueden almacenar los datos utilizando estructuras de datos complejas como los árboles k-d para hacer que la búsqueda y coincidencia de nuevos patrones durante la predicción sea eficiente. 

Debido a que se almacena el conjunto completo de datos de entrenamiento, es posible que desee pensar cuidadosamente en la coherencia de sus datos de entrenamiento. Podría ser una buena idea curarlos, actualizarlos con frecuencia a medida que surjan nuevos datos y eliminar datos erróneos y atípicos.

## Realización de Predicciones
KNN realiza predicciones utilizando directamente el conjunto de datos de entrenamiento. Las predicciones se hacen para un nuevo punto de datos buscando en todo el conjunto de entrenamiento las K instancias más similares (los vecinos) y resumiendo la variable de salida para esas K instancias. Para la regresión, esto podría ser la media de la variable de salida, mientras que para la clasificación podría ser la moda (o el valor de clase más común).

Para determinar cuáles de las K instancias en el conjunto de datos de entrenamiento son más similares a una nueva entrada, se utiliza una medida de distancia. Para variables de entrada de valores reales, la medida de distancia más popular es la distancia euclidiana. La distancia euclidiana se calcula como la raíz cuadrada de la suma de las diferencias al cuadrado entre un punto a y un punto b en todos los atributos de entrada i.

$$ EuclideanDistance(a, b) = \sqrt{\sum_{i=1}^{n}(a_i - b_i)^2 } $$

Otras medidas de distancia populares incluyen:

- **Distancia de Hamming:** Calcula la distancia entre vectores binarios.
- **Distancia de Manhattan:** Calcula la distancia entre vectores reales utilizando la suma de sus diferencias absolutas. También llamada distancia de bloque de la ciudad.
- **Distancia de Minkowski:** Generalización de la distancia euclidiana y de Manhattan

Existen muchas otras medidas de distancia que se pueden utilizar, como Tanimoto, Jaccard, Mahalanobis y distancia de coseno. Se puede elegir la mejor métrica de distancia en función de las propiedades de los  datos. Si no se está seguro, se puede experimentar con diferentes métricas de distancia y diferentes valores de K juntos y ver qué combinación produce los modelos más precisos. 

- La distancia euclidiana es una buena medida de distancia para usar si las variables de entrada son similares en tipo (como todas las alturas o pesos).

- La distancia de Manhattan es una buena medida para usar si las variables de entrada no son similares en tipo (como edad, género, altura, etc.).

- El valor de K se puede encontrar mediante ajuste de algoritmo. Es una buena idea probar muchos valores diferentes para K (por ejemplo, valores del 1 al 21) y ver qué funciona mejor para el problema. 

La complejidad computacional de KNN aumenta con el tamaño del conjunto de datos de entrenamiento. Para conjuntos de entrenamiento muy grandes, KNN se puede hacer estocástico tomando una muestra del conjunto de datos de entrenamiento a partir del cual calcular las K instancias más similares. 

## KNN para regresión
Cuando se utiliza KNN para problemas de regresión, la predicción se basa en la media o la mediana de las K instancias más similares.

## KNN para clasificación
Cuando se utiliza KNN para clasificación, la salida se puede calcular como la clase con la frecuencia más alta de las K instancias más similares. Cada instancia en esencia vota por su clase y se toma la clase con más votos como la predicción. Las probabilidades de clase se pueden calcular como la frecuencia normalizada de muestras que pertenecen a cada clase en el conjunto de las K instancias más similares para una nueva instancia de datos. Por ejemplo, en un problema de clasificación binaria (la clase es 0 o 1)

$$ p(clase = 0) = \frac{count(clase = 0)}{count(clase = 0) + count(clase = 1)} $$

## Maldición de la dimensionalidad o Curse of Dimensionality
KNN funciona bien con un pequeño número de variables de entrada (p), pero tiene dificultades cuando el número de entradas es muy grande. Cada variable de entrada se puede considerar una dimensión de un espacio de entrada p-dimensional. Por ejemplo, si tuvieras dos variables de entrada $X_1$ y $X_2$, el espacio de entrada sería de 2 dimensiones. }

A medida que aumenta el número de dimensiones, el volumen del espacio de entrada aumenta a una tasa exponencial. En dimensiones altas, los puntos que pueden ser similares pueden tener distancias muy grandes. 

Todos los puntos estarán lejos unos de otros y nuestra intuición para las distancias en espacios simples de 2 y 3 dimensiones se rompe. Esto puede parecer poco intuitivo al principio, pero este problema general se llama Curse of Dimensionality

##  Preparación de Datos
- **Reescalar los datos:** KNN funciona mucho mejor si todos los datos tienen la misma escala. Normalizar los datos al rango entre 0 y 1 es una buena idea. También puede ser una buena idea estandarizar los datos si tienen una distribución gaussiana.

- **Datos faltantes:** Los datos faltantes significan que no se puede calcular la distancia entre muestras. Estas muestras podrían ser excluidas o los valores faltantes podrían ser imputados.

- **Reducir la dimensionalidad:** KNN es adecuado para datos de baja dimensionalidad.