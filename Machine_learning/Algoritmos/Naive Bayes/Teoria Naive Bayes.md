# Naive Bayes

## Introducción al teorema de Bayes
En machine learning a menudo  se esta interesado en seleccionar la mejor hipótesis (h) dada una serie de datos (d). En un problema de clasificación, la hipótesis (h) puede ser la clase que se le asigna a una nueva instancia de datos (d). Una de las formas más sencillas de seleccionar la hipótesis más probable dada la información que se tiene es utilizar el conocimiento previo que se tiene sobre el problema. El teorema de Bayes proporciona una manera de calcular la probabilidad de una hipótesis dada la información previa. El teorema de Bayes se formula de la siguiente manera:

$$ P(h|d) = \frac{P(d|h) \times P(h)}{P(d)} $$

Donde:
- $P(h|d)$ es la probabilidad de la hipótesis h dados los datos d. Se denomina probabilidad posterior
- $P(s|h)$ es la probabilidad de los datos d dado que la hipótesis h era cierta
- $P(h)$ es la probabilidad de que la hipótesis h sea cierta (independientemente de los datos). Se denomina
probabilidad a priori de h.
- $P(d)$ es la probabilidad de los datos (independientemente de la hipótesis).

Se puede observar que se esta interesado en calcular la probabilidad posterior de $P(h|d)$ a partir de la probabilidad previa $p(h)$ con $P(D)$ y $P(d|h)$. 

Después de calcular la probabilidad posterior para varias hipótesis diferentes, se puede seleccionar la hipótesis con la probabilidad más alta. Esta es la hipótesis más probable y se puede denominar formalmente como la hipótesis a posteriori máxima (MAP). Esto se escribe como:

$$\begin{align*}
MAP(h) &= max(P(h|d))\\
MAP(h) &= max\left(\frac{P(d|h)\times P(h)}{P(d)}\right)\\
MAP(h) &= max(P(d|h)\times P(h))
\end{align*}$$

La expresión P(d) es un término de normalización que permite calcular la probabilidad. Se puede omitir cuando se esta interesado en la hipótesis más probable, ya que es una constante y solo se utiliza para normalizar. En cuanto a la clasificación, si se tiene un número par de instancias en cada clase de los datos de entrenamiento, entonces la probabilidad de cada clase (por ejemplo, P(h)) será el mismo valor para cada clase (por ejemplo, 0.5 para una división 50-50). Nuevamente, este sería un término constante en la ecuación y se puede eliminar para obtener:

$$ MAP(h) = max(P(d|h))$$

## Clasificador Naive Bayes
Naive Bayes es un algoritmo de clasificación binaria y clasificación multiclase. La técnica es más fácil de entender cuando se describen los valores de entrada de forma binaria. 

Se llama naive Bayes o Bayes ingenuo porque el cálculo de las probabilidades para cada hipótesis se simplifica para que sea factible su cálculo. En lugar de intentar calcular los valores de cada valor de atributo $P(d1, d2, d3|h)$, se realiza la suposición que son condicionalmente independientes dado el valor objetivo y se calculan como $P(d1|h) \times P (d2|h)$ y así sucesivamente. Esta es una suposición muy fuerte que es poco probable en datos reales, es decir, que los atributos no interactúan. Sin embargo, el enfoque funciona sorprendentemente bien en datos donde esta suposición no se cumple.

### Representación utilizada por los modelos Naive Bayes

La representación para Naive Bayes son las probabilidades. Una lista de probabilidades se almacena en un archivo para un modelo de Naive Bayes aprendido. Esto incluye:

- **Probabilidades de clase:** las probabilidades de cada clase en el conjunto de datos de entrenamiento.

- **Probabilidades condicionales:** las probabilidades condicionales de cada valor de entrada dado cada valor de clase.

### Como aprende el modelo a partir de los datos
El entrenamiento es rápido porque solo se necesitan calcular la probabilidad de cada clase y la probabilidad de cada clase dada diferentes valores de entrada (x). No se necesitan ajustar coeficientes mediante procedimientos de optimización.

#### Cálculo de las Probabilidades de Clase
Las probabilidades de clase son simplemente la frecuencia de instancias que pertenecen a cada clase dividida por el número total de instancias. Por ejemplo, en una clasificación binaria, la probabilidad de que una instancia pertenezca a la clase 1 se calcularía como:

$$ P(clase = 1) = \frac{count(clase = 1)}{count(clase = 0) + count(clase = 1)}$$

#### Cálculo de probabilidades condicionales
Las probabilidades condicionales son la frecuencia de cada valor de atributo para un valor de clase dado dividido por la frecuencia de instancias con ese valor de clase. Por ejemplo, si un atributo del clima tenía los valores soleado y lluvioso y el atributo de clase tenía los valores de clase salir y quedarse en casa, entonces las probabilidades condicionales de cada valor de clima para cada valor de clase se podrían calcular como:

$$\begin{align*}
P(clima=soleado|calse=salir) &= \frac{count(clima=soleado\ \wedge\ clase=salir}{count(clase=salir)}\\

P(clima=soleado|calse=quedarse) &= \frac{count(clima=soleado\ \wedge\ clase= quedarse}{count(clase=quedarse)}\\

P(clima=lluvioso|calse = salir) &= \frac{count(clima=lluvioso\ \wedge\ clase= salir}{count(clase=salir)}\\

P(clima=lluvioso|calse=quedarse) &= \frac{count(clima=lluvioso\ \wedge\ clase=quedarse}{count(clase=quedarse)}\\
\end{align*}$$

#### Hacer predicciones con naive Bayes
Dado un modelo naive Bayes, puede hacer predicciones para nuevos datos utilizando el teorema de Bayes.

$$ MAP(h) = max(P(d|h)\times P(h)) $$

Utilizando el ejemplo anterior, si se tuviera una nueva instancia con el tiempo soleado, se puede calcular:

$$\begin{align*}
salir &= P(clima=soleado|clase=salir) \times P(clase=salir)\\
quedarse &= P(clima=soleado|clase=quedarse) \times P(clase=quedarse)
\end{align*}$$

Se elegir la clase que tenga el mayor valor calculado y se puede normalizar los valores de la siguiente manera:

$$\begin{align*}
P(salir|clima=soleado) &= \frac{salir}{salir+quedarse}\\
P(quedarse|clima=soleado) &= \frac{quedarse}{salir+quedarse}\\
\end{align*}$$

Si tienes más variables de entrada, puedes extender el ejemplo anterior. Por ejemplo, imagina que tienes un atributo de auto con los valores "funcionando" y "averiado". Puedes multiplicar esta probabilidad en la ecuación. A continuación se muestra el cálculo para la etiqueta de clase "salir" con la adición de la variable de entrada del coche establecida en "funcionamiento".

$$\begin{align*}
salir = &P(clima=soleado|clase=salir) \times \\
&P(auto = funcionando|clase = salir) \times \\
&P(clase = salir)
\end{align*}$$

## Gaussian Naive Bayes
Naive Bayes puede extenderse a atributos de valores reales, más comúnmente asumiendo una distribución Gaussiana. Esta extensión se llama Naive Bayes Gaussiano. Se pueden usar otras funciones para estimar la distribución de los datos, pero la distribución Gaussiana (o Normal) es la más fácil de trabajar porque solo se necesita estimar la media y la desviación estándar de los datos de entrenamiento.

### Representación para Naive Bayes Gaussiano
Anteriormente, se calcularon las probabilidades para los valores de entrada para cada clase utilizando una frecuencia. Con entradas de valores reales, se puede calcular la media y la desviación estándar de los valores de entrada (x) para cada clase para resumir la distribución. Esto significa que, además de las probabilidades para cada clase, también se debe almacenar la media y la desviación estándar para cada variable de entrada para cada clase.

### Como aprende Naive Bayes Gaussiano a partir de los datos
Esto es tan simple como calcular los valores de media y desviación estándar de cada variable de entrada (x) para cada valor de clase.

$$ media(x) = \frac{1}{n} \sum_{i=1}^{n} x_i$$

Donde n es el número de instancias y x son los valores de una variable de entrada en tus datos de entrenamiento. Podemos calcular la desviación estándar usando la siguiente ecuación:

$$ desviación Estándar(x) = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i - media(x))^2 } $$

Esta es la raíz cuadrada de la diferencia media cuadrada de cada valor de x respecto al valor medio de x, donde n es el número de instancias, $x_i$ es un valor específico de la variable x para la i-ésima instancia y media(x) se describe arriba.

### Realizar predicciones con un modelo de Naive Bayes Gaussiano
Las probabilidades de nuevos valores x se calculan utilizando la función de densidad de probabilidad Gaussiana (PDF). Al hacer predicciones, estos parámetros se pueden insertar en la PDF Gaussiana con una nueva entrada para la variable y, a cambio, la PDF Gaussiana proporcionará una estimación de la probabilidad de ese nuevo valor de entrada para esa clase

$$ pdf(x,\mu,\sigma) = \frac{1}{\sqrt{2\pi \sigma}} e^{-\left(\frac{(x-\mu)^2}{2\sigma^2} \right)}$$

## Preparando los Datos para Naive Bayes
Esta sección proporciona algunos consejos para preparar datos para Naive Bayes.

- **Entradas Categóricas:** Naive Bayes asume atributos de etiqueta como binarios, categóricos o nominales.
- **Entradas Gaussianas:** Si las variables de entrada son de valores reales, se asume una distribución gaussiana. En este caso, el algoritmo funcionará mejor si las distribuciones univariadas de tus datos son gaussianas o cercanas a la gaussiana.
- **Probabilidades Logarítmicas:** El cálculo de la probabilidad de diferentes valores de clase implica multiplicar muchos números pequeños juntos. Esto puede conducir a una subfluencia de precisión numérica. Por lo tanto, es buena práctica utilizar una transformación logarítmica de las probabilidades para evitar esta subfluencia.
- **Funciones Kernel:** En lugar de asumir una distribución gaussiana para valores de entrada numéricos, se pueden utilizar distribuciones más complejas como una variedad de funciones de densidad de kernel.
- **Actualización de las probabilidades:** Cuando se dispone de nuevos datos, simplemente se pueden actualizar las probabilidades de tu modelo. Esto puede ser útil si los datos cambian con frecuencia.