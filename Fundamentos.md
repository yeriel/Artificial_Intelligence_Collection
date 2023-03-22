# Fundamentos del machine learning

## ¿Que es el ML?
El Machine Learning (Aprendizaje Automático, en español) es una rama de la inteligencia artificial que se centra en el estudio de los algoritmos y modelos que permiten a los sistemas informáticos aprender y mejorar su rendimiento en tareas específicas a partir de los datos, sin la necesidad de ser programados explícitamente. En otras palabras, el Machine Learning permite a las maquinas aprender a través de la experiencia, como lo hace un ser humano.

Un definición un poco mas formal de esta disciplina es la que propone Mitchell (1997). "Un programa informático se dice que aprende a partir de la experiencia E con respecto a alguna clase de tareas T y medida de rendimiento P, si su rendimiento en tareas de T, medido por P, mejora con la experiencia E".

En esta definición relativamente formal de la palabra "tarea" T, el proceso de aprendizaje en sí no es la tarea. El aprendizaje es el medio para adquirir la capacidad de realizar la tarea. Por ejemplo, si queremos que un robot sea capaz de caminar, entonces caminar es la tarea.

También se debe evaluar las habilidades de un algoritmo, para ello se diseña una medida cuantitativa de su rendimiento. Por lo general, esta medida de rendimiento P es específica para la tarea T que está llevando a cabo el sistema.

En cuanto a la experiencia E corresponde al entrenamiento que tiene el sistema para lograr realizar la tarea T.

### La tarea T
Se pueden resolver muchos tipos de tareas. Algunas de las tareas más comunes de Machine Learning incluyen las siguientes:

- **Clasificación:** En este tipo de tarea, se le pide a la maquina que especifique a qué categoría pertenece alguna entrada de k categorías. Para resolver esta tarea, generalmente se le pide al algoritmo de aprendizaje que produzca una función $f: R^n \to \{ 1, \dots, k\}$. Cuando $y = f(x)$, el modelo asigna una entrada descrita por el vector $x$ a una categoría identificada por el código numérico. Existen otras variantes de la tarea de clasificación, por ejemplo, donde $f$ devuelve una distribución de probabilidad sobre las clases.

- **Regresión:** En este tipo de tarea, se le pide a la maquina que prediga un valor numérico dado cierta entrada. Para resolver esta tarea, se le pide al algoritmo de aprendizaje que genere una función $f: R^n \to R$.

- **Transcripción:** En este tipo de tarea, se le pide a la maquina que observe una representación relativamente no estructurada de algún tipo de datos y lo transcriba en forma textual discreta.

- **Detección de anomalías:** En este tipo de tarea, la maquina examina un conjunto de eventos u objetos y marca algunos de ellos como inusuales o atípicos.

- **Denoising:** En este tipo de tarea, el algoritmo de aprendizaje automático recibe como entrada un ejemplo corrupto obtenido mediante un proceso de corrupción desconocido a partir de un ejemplo limpio. El modelo debe predecir el ejemplo limpio a partir de su versión corrupta, o más generalmente, predecir la distribución de probabilidad condicional.