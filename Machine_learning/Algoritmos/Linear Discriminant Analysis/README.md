# Linear Discriminant Analysis

La regresión logística es un algoritmo de clasificación lineal simple y poderoso. Sin embargo, tiene limitaciones que sugieren la necesidad de algoritmos de clasificación lineal alternativos.

- **Problemas de dos clases:** La regresión logística está diseñada para problemas de clasificación binaria o de dos clases. Se puede extender para la clasificación multiclase, pero rara vez se utiliza para este propósito.
- **Inestable con clases bien separadas:** La regresión logística puede volverse inestable cuando las clases están bien separadas.
- **Inestable con pocos ejemplos:** La regresión logística puede volverse inestable cuando hay pocos ejemplos para estimar los parámetros.

El análisis discriminante lineal aborda cada uno de estos puntos y es el método lineal preferido para problemas de clasificación multiclase. Incluso con problemas de clasificación binaria, es una buena idea probar tanto la regresión logística como el análisis discriminante lineal.

## Aprendizaje de LDA

LDA hace algunas suposiciones simplificadas sobre tus datos:
- Que tus datos son gaussianos, es decir, que cada variable tiene forma de campana cuando se traza.
- Que cada atributo tiene la misma varianza, es decir, que los valores de cada variable varían alrededor de la media en la misma cantidad en promedio.

Con estas suposiciones, el modelo LDA estima la media y la varianza de tus datos para cada clase. Es fácil pensar en esto en el caso univariate (variable de entrada única) con dos clases. El valor medio (media) de cada entrada $x$ para cada clase $k$ se puede estimar de manera normal dividiendo la suma de valores por el número total de valores.

$$ \mu_k = \frac{1}{n_k}\sum_{i=1}^{n}x_i$$

Donde $\mu_k$ es el valor medio de $x$ para la clase $k$, $n_k$ es el número de instancias con la clase $k$. La varianza se calcula en todas las clases como la media de la diferencia al cuadrado de cada valor respecto a la media.

$$ \sigma^2 = \frac{1}{n-K}\sum_{i=1}^{n}(x_i - \mu_k)^2$$

Donde $\sigma^2$ es la varianza de todas las entradas $x$, $n$ es el número de instancias, $K$ es el número de clases y $\mu_k$ es la media de $x$ para la clase a la que pertenece $x_i$. En otras palabras, calculamos la diferencia al cuadrado de cada valor respecto a la media dentro de los grupos de clases, pero promediamos estas diferencias en todos los grupos de clases. Recuerda que cuando hablamos de varianza las unidades son unidades al cuadrado, no que necesitamos elevar al cuadrado el valor de la varianza.

## Predicciones con LDA

LDA realiza predicciones estimando la probabilidad de que un nuevo conjunto de entradas pertenezca a cada clase. La clase que obtiene la probabilidad más alta es la clase de salida y se realiza una predicción. El modelo utiliza el teorema de Bayes para estimar las probabilidades. En resumen, el teorema de Bayes se puede utilizar para estimar la probabilidad de la clase de salida $k$ dada la entrada $x$ utilizando la probabilidad de cada clase y la probabilidad de que los datos pertenezcan a cada clase:

$$ P(Y = k\ | X = x) = \frac{P(k) P(x\ |\ k)}{\sum_{i=1}^{K}\left(P(l)P(x\ |\ l)\right)}$$

Donde:

- $P(Y=k\ |\ X=x)$ es la probabilidad de la clase $Y=k$ dada la entrada de datos $x$.

- $P(k)$ es la probabilidad base de una clase $k$ determinada que estamos considerando $Y=k$, por ejemplo, la proporción de instancias con esta clase en el conjunto de datos de entrenamiento.

- $P(x\ |\ k)$ es la probabilidad estimada de que $x$ pertenezca a la clase $k$

- El denominador normaliza para cada clase $l$, es decir, la probabilidad de la clase $P(l)$ y la probabilidad de la entrada dada la clase $P(x\ |\ l)$.

- Se puede utilizar una función de distribución gaussiana para estimar $P(x\ |\ k)$. Al enchufar la gaussiana en la ecuación anterior y simplificar, obtenemos la siguiente ecuación. Ya no es una probabilidad ya que descartamos algunos términos. En cambio, se llama función discriminante para la clase $k$. Se calcula para cada clase $k$ y la clase que tiene el valor de discriminante más grande hará la clasificación de salida $Y=k$

$$D_k(x) = x\frac{\mu_k}{\sigma^2} - \frac{\mu_k^2}{2\sigma^2} + ln\left(P(k)\right)$$

$D_k(x)$ es la función discriminante para la clase $k$ dada la entrada $x$, $\mu_k$, $\sigma^2$ y $P(k)$ se estiman a partir de los datos.

## Preparando los datos para LDA

Esta sección enumera algunas sugerencias que puede considerar al preparar sus datos para usar con LDA.

- **Problemas de clasificación:** Esto puede parecer obvio, pero LDA está destinado a problemas de clasificación donde la variable de salida es categórica. LDA admite tanto clasificación binaria como multicategoría.

- **Distribución gaussiana:** La implementación estándar del modelo asume una distribución gaussiana de las variables de entrada. Considere revisar las distribuciones univariadas de cada atributo y usar transformaciones para hacer que se parezcan más a una distribución gaussiana.

- **Eliminar valores atípicos:** Considere eliminar los valores atípicos de sus datos. Estos pueden sesgar las estadísticas básicas utilizadas para separar las clases en LDA, como la media y la desviación estándar.

- **Varianza igual:** LDA asume que cada variable de entrada tiene la misma varianza. Casi siempre es una buena idea estandarizar sus datos antes de usar LDA para que tengan una media de 0 y una desviación estándar de 1.
