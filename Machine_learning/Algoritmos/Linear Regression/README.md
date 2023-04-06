# Linear Regression

## ¿No es la regresión lineal de la estadística?

Antes de profundizar en los detalles de la regresión lineal, es posible que te preguntes por qué estamos viendo este algoritmo. ¿No es una técnica de la estadística?
El aprendizaje automático, específicamente el campo del modelado predictivo, se preocupa principalmente por minimizar el error de un modelo o hacer las predicciones más precisas posibles, a expensas de la explicabilidad.

Como tal, la regresión lineal se desarrolló en el campo de la estadística y se estudia como un modelo para comprender la relación entre variables numéricas de entrada y salida, pero ha sido tomado prestado por el aprendizaje automático. Es tanto un algoritmo estadístico como un algoritmo de aprendizaje automático. A continuación, revisemos algunos de los nombres comunes que se usan para referirse a un modelo de regresión lineal.

## Muchos nombres de la regresión lineal

Cuando comienzas a investigar la regresión lineal, las cosas pueden volverse muy confusas. La razón es que la regresión lineal ha existido durante tanto tiempo (más de 200 años). Se ha estudiado desde todos los ángulos posibles y a menudo cada ángulo tiene un nombre nuevo y diferente.

La regresión lineal es un modelo lineal, es decir, un modelo que asume una relación lineal entre las variables de entrada (x) y la variable de salida única (y). Más específicamente, que y se puede calcular a partir de una combinación lineal de las variables de entrada (x). Cuando hay una sola variable de entrada (x), el método se conoce como regresión lineal simple. Cuando hay múltiples variables de entrada, la literatura de estadísticas a menudo se refiere al método como regresión lineal múltiple.

Se pueden utilizar diferentes técnicas para preparar o entrenar la ecuación de regresión lineal a partir de los datos, la más común de las cuales se llama Mínimos Cuadrados Ordinarios. Es común referirse a un modelo preparado de esta manera como Regresión Lineal de Mínimos Cuadrados Ordinarios o simplemente Regresión de Mínimos Cuadrados. Ahora que conocemos algunos nombres utilizados para describir la regresión lineal, echemos un vistazo más de cerca a la representación utilizada.

## Representación del modelo de Regresión Lineal

La regresión lineal es un modelo atractivo porque la representación es muy simple. La representación es una ecuación lineal que combina un conjunto específico de valores de entrada $x$, cuya solución es la salida predicha para ese conjunto de valores de entrada $y$. Como tal, tanto los valores de entrada $x$ como la salida son numéricos.

La ecuación lineal asigna un factor de escala a cada valor de entrada o columna, llamado coeficiente, que comúnmente se representa con la letra griega Beta $\beta$. Se agrega un coeficiente adicional, dando a la línea un grado adicional de libertad (por ejemplo, moviéndose hacia arriba y hacia abajo en un gráfico bidimensional) y a menudo se llama el intercepto o el coeficiente de sesgo. Por ejemplo, en un problema de regresión simple (un solo x y un solo y), la forma del modelo sería:

$$y = B_0 + B_1 × x $$

En dimensiones más altas cuando tenemos más de una entrada $x$, la línea se llama plano o hiperplano. La representación, por lo tanto, es la forma de la ecuación y los valores específicos utilizados para los coeficientes (por ejemplo, $B_0$ y $B_1$ en el ejemplo anterior). Es común hablar sobre la complejidad de un modelo de regresión como la regresión lineal. Esto se refiere al número de coeficientes utilizados en el modelo.

Cuando un coeficiente se vuelve cero, elimina efectivamente la influencia de la variable de entrada en el modelo y, por lo tanto, en la predicción realizada a partir del modelo $0 × x = 0$. Esto se vuelve relevante si se observan los métodos de regularización que cambian el algoritmo de aprendizaje para reducir la complejidad de los modelos de regresión ejerciendo presión sobre el tamaño absoluto de los coeficientes, llevando algunos a cero. Ahora que entendemos la representación utilizada para un modelo de regresión lineal, revisemos algunas formas en que podemos aprender esta representación a partir de los datos.

## Entrenamiento Regression Learning

El entrenamiento de Regression Learning  significa estimar los valores de los coeficientes utilizados en la representación con los datos que tenemos disponibles. En esta sección, echaremos un vistazo breve a cuatro técnicas para preparar un modelo de regresión lineal. 

### Regresión Lineal Simple

Con regresión lineal simple, cuando tenemos una sola entrada, podemos usar estadísticas para estimar los coeficientes. Esto requiere que se calculen propiedades estadísticas de los datos, como promedios, desviaciones estándar, correlaciones y covarianzas. Todos los datos deben estar disponibles para recorrerlos y calcular las estadísticas. Esto puede ser divertido como un ejercicio en una hoja de cálculo, pero no es realmente útil en la práctica.

### Mínimos Cuadrados Ordinarios

Cuando tenemos más de una entrada, podemos usar Mínimos Cuadrados Ordinarios para estimar los valores de los coeficientes. El procedimiento de Mínimos Cuadrados Ordinarios busca minimizar la suma de los residuos cuadrados. Esto significa que, dada una línea de regresión a través de los datos, calculamos la distancia de cada punto de datos a la línea de regresión, la elevamos al cuadrado y sumamos todos los errores cuadrados juntos. Esta es la cantidad que los Mínimos Cuadrados Ordinarios buscan minimizar.

Este enfoque trata los datos como una matriz y utiliza operaciones de álgebra lineal para estimar los valores óptimos de los coeficientes. Esto significa que todos los datos deben estar disponibles y que se debe tener suficiente memoria para ajustar los datos y realizar operaciones de matriz. Es poco común implementar el procedimiento de Mínimos Cuadrados Ordinarios por uno mismo, a menos que sea como un ejercicio de álgebra lineal.

### Descenso del gradiente

Cuando hay uno o más entradas, puedes utilizar un proceso para optimizar los valores de los coeficientes al minimizar iterativamente el error del modelo en tus datos de entrenamiento. Esta operación se llama Descenso del Gradiente y funciona empezando con valores de cero para cada coeficiente. La suma de los errores al cuadrado se calcula para cada par de valores de entrada y salida. Se utiliza una tasa de aprendizaje como factor de escala y los coeficientes se actualizan en la dirección hacia la minimización del error. El proceso se repite hasta que se logra un mínimo de la suma de los errores al cuadrado o no se puede obtener más mejora.

Cuando utilizas este método, debes seleccionar un parámetro de tasa de aprendizaje (alfa $\alpha$) que determina el tamaño del paso de mejora a tomar en cada iteración del procedimiento. El descenso del gradiente se enseña a menudo utilizando un modelo de regresión lineal porque es relativamente fácil de entender. En la práctica, es útil cuando tienes un conjunto de datos muy grande, ya sea en el número de filas o en el número de columnas, que no se puede almacenar en memoria.

### Regresión Lineal Regularizada
Existen extensiones del entrenamiento del modelo lineal llamadas métodos de regularización.

Estos buscan minimizar tanto la suma del error cuadrático del modelo en los datos de entrenamiento (utilizando Mínimos Cuadrados Ordinarios), como también reducir la complejidad del modelo (como el número o tamaño absoluto de la suma de todos los coeficientes del modelo). Dos ejemplos populares de procedimientos de regularización para la regresión lineal son:

- **Regresión Lasso:** donde Mínimos Cuadrados Ordinarios se modifica para minimizar también la suma absoluta de los coeficientes (llamada regularización L1).

- **Regresión Ridge:** donde Mínimos Cuadrados Ordinarios se modifica para minimizar también la suma absoluta al cuadrado de los coeficientes (llamada regularización L2).

Estos métodos son efectivos cuando hay colinealidad en los valores de entrada y los Mínimos Cuadrados Ordinarios sobreajustarían los datos de entrenamiento. Ahora que conoces algunas técnicas para aprender los coeficientes en un modelo de regresión lineal, veamos cómo podemos usar un modelo para hacer predicciones sobre nuevos datos. 

## Hacer predicciones 

Dada la representación de una ecuación lineal, hacer predicciones es tan simple como resolver la ecuación para un conjunto específico de entradas. Veamos un ejemplo concreto. Imaginemos que estamos prediciendo el peso (y) a partir de la altura (x). La representación de nuestro modelo de regresión lineal para este problema sería:

$$peso = B_0 + B_1 × altura$$ 

Donde $B_0$ es el coeficiente de sesgo y $B_1$ es el coeficiente para la columna de altura. Utilizamos una técnica de aprendizaje para encontrar un buen conjunto de valores de coeficientes. Una vez encontrados, podemos introducir diferentes valores de altura para predecir el peso. Por ejemplo, usemos $B_0 = 0,1$ y $B_1 = 0,5$. Introdúzcalos y calculemos el peso (en kilogramos) para una persona con una altura de 182 centímetros.

$$peso = 0,1 + 0,05 × 182$$
$$peso = 91,1$$

Se puede observar que la ecuación anterior podría representarse gráficamente como una línea en dos dimensiones. El $B_0$ es nuestro punto de partida independientemente de la altura que tengamos. Podemos pasar por una serie de alturas desde 100 hasta 250 centímetros e introducirlas en la ecuación y obtener valores de peso, creando así nuestra línea.

Ahora que sabemos cómo hacer predicciones con un modelo de regresión lineal aprendido, veamos algunas reglas generales para preparar nuestros datos para aprovechar al máximo este tipo de modelo.

## Preparación de los datos

- **Suposición Lineal:** La regresión lineal supone que la relación entre su entrada y salida es lineal. No admite otra cosa. Esto puede ser obvio, pero es bueno recordarlo cuando se tienen muchos atributos. Puede ser necesario transformar los datos para hacer que la relación sea lineal.

- **Eliminar Ruido:** La regresión lineal supone que sus variables de entrada y salida no tienen ruido. Considere utilizar operaciones de limpieza de datos que le permitan exponer y clarificar mejor la señal en sus datos. Esto es especialmente importante para la variable de salida y desea eliminar valores atípicos en la variable de salida y si es posible.

- **Eliminar Colinealidad:** La regresión lineal ajustará demasiado sus datos cuando tenga variables de entrada altamente correlacionadas. Considere calcular correlaciones por pares para sus datos de entrada y eliminar las más correlacionadas.

- **Distribuciones Gaussianas:** La regresión lineal hará predicciones más confiables si sus variables de entrada y salida tienen una distribución gaussiana.

- **Reescalar las entradas:** La regresión lineal a menudo hará predicciones más confiables si reescala las variables de entrada utilizando la estandarización o normalización.