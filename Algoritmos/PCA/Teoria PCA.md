# Principal component Analysis PCA
En escenarios del mundo real, las tareas de análisis de datos implican análisis de datos complejos, es decir, análisis de datos multidimensionales.

A medida que aumentan las dimensiones de los datos, también aumenta la dificultad de visualizarlos y realizar cálculos sobre ellos. Entonces, ¿cómo reducir las dimensiones de los datos?

- Eliminar la dimensión redundante.
- Solo mantener la dimensión más importante.

Para reducir las dimensiones de los datos, se utiliza el análisis de componentes principales PCA. Antes de profundizar en el funcionamiento de PCA, se debe tener claro los siguiente conceptos.

## Varianza
Es una medida de la variabilidad o simplemente mide que tan disperso está el conjunto de datos.  

$$ var(x) = \frac{\sum(x_i - \bar{x})^2}{N} $$

## Covarianza
Es una medida estadística que indica la relación lineal entre dos variables aleatorias. Representa la medida en la que dos variables cambian juntas, es decir, si una variable aumenta, ¿la otra también tiende a aumentar o a disminuir? Una covarianza positiva indica que las variables cambian en la misma dirección, mientras que una covarianza negativa indica que cambian en direcciones opuestas.

$$ cov(x,y) = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{N}$$

## Los vectores propios y valores propios
En álgebra lineal, los vectores propios y valores propios son propiedades de una transformación lineal o de una matriz cuadrada. Un vector propio es un vector que, cuando se transforma por una matriz, mantiene su dirección, es decir, no cambia de dirección, pero puede ser multiplicado por un escalar, que se llama valor propio, que indica cuánto se estira o se contrae el vector. 

$$ A\vec{v} = \lambda \vec{v}$$

## Algoritmo PCA 
1. Calcular la matriz de covarianza X de los datos.
2. Calcular los vectores propios y los valores propios correspondientes.
3. Ordenar los vectores propios según sus valores propios en orden decreciente.
4. Elegir los primeros k vectores propios y esos serán las nuevas k dimensiones.
5. Transformar los datos originales de n dimensiones en k dimensiones.

Para ver un detalle matemático breve de como realizar la descomposición de valores propios ver los apuntes de [algebra lineal](https://gist.github.com/yeriel/b82b7a67f9b2e38ac84f5d2248f50c52) y para mayor detalle recomendando estos [videos](https://www.youtube.com/playlist?list=PLmZlBIcArwhMfNuMBg4XR-YQ0QIqdHCrl)

## ¿Cuándo usar PCA?
- Si se busca reducir el número de variables, pero no se puede identificar las variables para ser eliminar.
- Si se quiere que sus variables sean independientes entre sí.
- Para evitar el sobreajuste del modelo.
- Cuando no se tiene problema con que las variable independiente sea menos interpretable.

### Ventajas
- **Remueve características correlacionadas:** En un escenario del mundo real, es común tener miles de características en el conjunto de datos. No se puede ejecutar un algoritmo en todas las características, ya que esto reducirá el rendimiento del algoritmo y no será fácil visualizar tantas características en cualquier tipo de gráfico. Por lo tanto, se debe reducir el número de características en el conjunto de datos. 

- **Mejora el rendimiento del algoritmo:** Con tantas características, el rendimiento de un algoritmo disminuirá drásticamente. PCA es una forma muy común de acelerar un algoritmo de Machine Learning eliminando las variables correlacionadas que no contribuyen en la toma de decisiones.

- **Mejora la visualización:** Es muy difícil visualizar y comprender los datos en dimensiones altas. PCA transforma los datos de alta dimensionalidad a datos de baja dimensionalidad (2 dimensiones) para que puedan visualizarse fácilmente.

### Desventajas
- **Las variables independientes se vuelven menos interpretables:** Después de implementar PCA en el conjunto de datos, sus características originales se convertirán en Componentes Principales. Estas son la combinación lineal de sus características originales lo que implica que no son tan legibles e interpretables como las características originales.

- **La estandarización de datos es necesaria antes de PCA:** Debe estandarizar sus datos antes de implementar PCA, de lo contrario PCA no podrá encontrar las Componentes Principales óptimas. 

- **Pérdida de información:** aunque las Componentes Principales intentan cubrir la máxima varianza entre las características en un conjunto de datos, si no seleccionamos el número de Componentes Principales con cuidado, puede perder información en comparación con la lista original de características.