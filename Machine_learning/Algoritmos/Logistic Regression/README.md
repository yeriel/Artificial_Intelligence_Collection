# Logistic Regression

La regresión logística lleva el nombre de la función logística. La función logística, también llamada función sigmoide, fue desarrollada por estadísticos para describir las propiedades del crecimiento de la población en ecología, aumentando rápidamente y alcanzando su máximo en la capacidad de carga del medio ambiente. Es una curva en forma de S que puede tomar cualquier número de valor real y asignarlo a un valor entre 0 y 1, pero nunca exactamente en esos límites.

$$\frac{1}{1+e^{-x}} $$

Donde e es la base de los logaritmos naturales (número de Euler) y valor es el valor numérico real que se desea transformar. A continuación, se muestra una gráfica de los números entre -8 y 0 transformados en el rango de 0 y 1 utilizando la función logística.

![logic regression](https://miro.medium.com/v2/resize:fit:720/format:webp/1*RqXFpiNGwdiKBWyLJc_E7g.png)

Ahora que sabemos qué es la función logística, veamos cómo se utiliza en la regresión logística.

## La Representación Utilizada para la Regresión Logística

La regresión logística utiliza una ecuación como representación, muy parecida a la regresión lineal. Los valores de entrada (x) se combinan linealmente usando pesos o valores de coeficientes para predecir un valor de salida $y$. Una diferencia clave con la regresión lineal es que el valor de salida que se modela es un valor binario en lugar de un valor numérico.

A continuación se muestra un ejemplo de ecuación de regresión logística:

$$ y = \frac{e^{
    B_0+B_1x
}}{1+e^{B_0+B_1x}} $$

Donde $y$ es la salida prevista, $B_0$ es el término de sesgo o de intercepción, y $B_1$ es el coeficiente para el único valor de entrada $x$. Cada columna en sus datos de entrada tiene un coeficiente $B$ asociado (un valor real constante) que debe ser aprendido a partir de sus datos de entrenamiento. La representación real del modelo que se almacenaría en la memoria o en un archivo son los coeficientes en la ecuación (el valor beta o $B$).

## La regresión logística predice probabilidades.

La regresión logística modela la probabilidad de la clase por defecto. Por ejemplo, si estamos modelando el sexo de las personas como masculino o femenino a partir de su altura, entonces la primera clase podría ser masculino y el modelo de regresión logística podría escribirse como la probabilidad de masculino dada la altura de una persona, o más formalmente:

$$ P(sexo = hombre\ |\ peso)$$

De otra manera, estamos modelando la probabilidad de que una entrada $X$ pertenezca a la clase por defecto $Y = 1$, lo cual podemos escribir formalmente como:

$$ P(X) = P(Y= 1\ |\ X)$$

¿Estamos prediciendo probabilidades? ¿No se suponía que la regresión logística era un algoritmo de clasificación?
Nótese que la predicción de probabilidad debe ser transformada en valores binarios para poder hacer una predicción clara. Hablaremos más sobre esto más adelante cuando hablemos de hacer predicciones. La regresión logística es un método lineal, pero las predicciones son transformadas usando la función logística. El impacto de esto es que ya no podemos entender las predicciones como una combinación lineal de las entradas como podemos hacerlo con la regresión lineal. Continuando desde el ejemplo anterior, el modelo puede ser establecido como:

$$p(X) = \frac{e^{B_0+B_1x}}{1+e^{B_0+B_1x}} $$

No quiero profundizar demasiado en las matemáticas, pero podemos desglosar la ecuación anterior de la siguiente manera (recuerde que podemos remover la e de un lado añadiendo un ln() al otro):

$$ ln\left(\frac{p(x)}{1-p(x)}\right) = B_0+B_1x$$

Esto es útil porque podemos ver que el cálculo de la salida del lado derecho es lineal nuevamente (como la regresión lineal), y la entrada del lado izquierdo es el logaritmo natural de la probabilidad de la clase por defecto. Esta proporción del lado izquierdo se llama las probabilidades de la clase por defecto.

Las probabilidades se calculan como una relación de la probabilidad del evento dividida por la probabilidad del no evento, por ejemplo, $\frac{0.8}{1-0.8}$ que tiene una probabilidad de 4. Por lo tanto, podemos escribir en su lugar:

$$ ln(probabilidad) = B_0+B_1x$$

Debido a que las probabilidades están logarítmicamente transformadas, llamamos a este lado izquierdo las log probabilidades o el probit. Es posible utilizar otros tipos de funciones para la transformación, pero como tal es común referirse a la transformación que relaciona la ecuación de regresión lineal con las probabilidades como la función de enlace, por ejemplo, la función de enlace logit. Podemos mover el exponente de vuelta al lado derecho y escribirlo como:

$$ Probabilidad = e^{B_0+B_1x}$$

Todo esto nos ayuda a entender que, de hecho, el modelo sigue siendo una combinación lineal de las entradas, pero que esta combinación lineal se relaciona con las log-probabilidades de la clase por defecto.

## Aprendizaje

Los coeficientes del algoritmo de regresión logística deben ser estimados a partir de los datos de entrenamiento. Esto se hace utilizando la estimación de máxima verosimilitud. La estimación de máxima verosimilitud es un algoritmo de aprendizaje común utilizado por una variedad de algoritmos de aprendizaje automático, aunque hace suposiciones sobre la distribución de sus datos.

Los mejores coeficientes resultarían en un modelo que predeciría un valor muy cercano a 1 (masculino) para la clase por defecto y un valor muy cercano a 0 (femenino) para la otra clase. La intuición para la máxima verosimilitud en la regresión logística es que un procedimiento de búsqueda busca valores para los coeficientes que minimizan el error en las probabilidades predichas por el modelo en comparación con las de los datos.

No vamos a entrar en los detalles matemáticos de la máxima verosimilitud. Es suficiente decir que se utiliza un algoritmo de minimización para optimizar los mejores valores de los coeficientes para los datos de entrenamiento. Esto a menudo se implementa en la práctica utilizando algoritmos de optimización numérica eficientes (como el método Quasi-Newton). Pero tambien se puede implantar el algoritmo de descenso de gradiente mucho más simple.

##  Preparación de datos para la regresión logística

Los supuestos que hace la regresión logística sobre la distribución y relaciones en los datos son muy similares a los supuestos hechos en la regresión lineal. Se ha dedicado mucho estudio a definir estos supuestos y se utiliza un lenguaje estadístico y probabilístico preciso. Mi consejo es usarlos como guías o reglas generales y experimentar con diferentes esquemas de preparación de datos.

- **Variable de salida binaria:** Esto puede ser obvio ya que lo hemos mencionado, pero la regresión logística está destinada a problemas de clasificación binaria (dos clases). Predecirá la probabilidad de que una instancia pertenezca a la clase predeterminada, que se puede clasificar como 0 o 1.

- **Eliminar ruido:** La regresión logística no asume errores en la variable de salida $y$, considere eliminar valores atípicos y posiblemente instancias mal clasificadas de sus datos de entrenamiento.

- **Distribución gaussiana:** la regresión logística es un algoritmo lineal (con una transformación no lineal en la salida). Supone una relación lineal entre las variables de entrada y la salida. Las transformaciones de datos de sus variables de entrada que expongan mejor esta relación lineal pueden resultar en un modelo más preciso.

- **Eliminar entradas correlacionadas:** al igual que la regresión lineal, el modelo puede sobreajustarse si tiene múltiples entradas altamente correlacionadas. Considere calcular las correlaciones de pares entre todas las entradas y eliminar las entradas altamente correlacionadas.

- **No converge:** es posible que el proceso de estimación de la verosimilitud esperada que aprende los coeficientes no converja. Esto puede suceder si hay muchas entradas altamente correlacionadas en sus datos o si los datos son muy dispersos (por ejemplo, muchos ceros en sus datos de entrada).
