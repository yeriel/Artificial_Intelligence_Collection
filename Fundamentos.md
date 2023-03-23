# Fundamentos del machine learning

Antes de adentrarse en el mundo del machine learning, es recomendable tener conocimientos sólidos en las disciplinas que lo sustentan, como el [álgebra lineal](https://gist.github.com/yeriel/b82b7a67f9b2e38ac84f5d2248f50c52) y el [cálculo numérico](https://gist.github.com/yeriel/f8473575ab8b2490b69f5e31569f655d). Estas son herramientas fundamentales para comprender y aplicar de manera efectiva los conceptos y algoritmos.

## ¿Que es el ML?
El Machine Learning (Aprendizaje Automático, en español) es una rama de la inteligencia artificial que se centra en el estudio de los algoritmos y modelos que permiten a los sistemas informáticos aprender y mejorar su rendimiento en tareas específicas a partir de los datos, sin la necesidad de ser programados explícitamente. En otras palabras, el Machine Learning permite a las maquinas aprender a través de la experiencia, como lo hace un ser humano.

Un definición un poco mas formal de esta disciplina es la que propone Mitchell (1997). "Un programa informático se dice que aprende a partir de la experiencia E con respecto a alguna clase de tareas T y medida de rendimiento P, si su rendimiento en tareas de T, medido por P, mejora con la experiencia E".

En esta definición relativamente formal la palabra "tarea" (T) se refiere a la actividad específica que se desea que un agente o sistema realice. El proceso de aprendizaje en sí no es la tarea en sí misma, sino un medio para adquirir la capacidad de realizar dicha tarea.

Por ejemplo, si deseamos que un robot sea capaz de caminar, entonces caminar es la tarea que se desea que el robot realice. El proceso de aprendizaje consistiría en enseñar al robot los movimientos necesarios para caminar y cómo aplicarlos en diferentes situaciones. Una vez que el robot ha aprendido a caminar, puede realizar la tarea en cualquier momento que se le solicite.

También se debe evaluar las habilidades de un algoritmo, para ello se diseña una medida cuantitativa de su rendimiento. Por lo general, esta medida de rendimiento P es específica para la tarea T que está llevando a cabo el sistema.

En cuanto a la experiencia E corresponde al entrenamiento que tiene el sistema para lograr realizar la tarea T.

### La tarea T
Se pueden resolver muchos tipos de tareas. Algunas de las tareas más comunes de Machine Learning incluyen las siguientes:

- **Clasificación:** En este tipo de tarea, se le pide a la maquina que especifique a qué categoría pertenece alguna entrada de k categorías. Para resolver esta tarea, generalmente se le pide al algoritmo de aprendizaje que produzca una función $f: R^n \to \{ 1, \dots, k\}$. Cuando $y = f(x)$, el modelo asigna una entrada descrita por el vector $x$ a una categoría identificada por el código numérico. Existen otras variantes de la tarea de clasificación, por ejemplo, donde $f$ devuelve una distribución de probabilidad sobre las clases.

- **Regresión:** En este tipo de tarea, se le pide a la maquina que prediga un valor numérico dado cierta entrada. Para resolver esta tarea, se le pide al algoritmo de aprendizaje que genere una función $f: R^n \to R$.

- **Transcripción:** En este tipo de tarea, se le pide a la maquina que observe una representación relativamente no estructurada de algún tipo de datos y lo transcriba en forma textual discreta.

- **Detección de anomalías:** En este tipo de tarea, la maquina examina un conjunto de eventos u objetos y marca algunos de ellos como inusuales o atípicos.

- **Denoising:** En este tipo de tarea, el algoritmo de aprendizaje automático recibe como entrada un ejemplo corrupto obtenido mediante un proceso de corrupción desconocido a partir de un ejemplo limpio. El modelo debe predecir el ejemplo limpio a partir de su versión corrupta, o más generalmente, predecir la distribución de probabilidad condicional.

### La experiencia E
Los algoritmos de machine learning pueden categorizarse ampliamente como supervisados o no supervisados según el tipo de experiencia que se les permita tener durante el proceso de aprendizaje.

- **Aprendizaje no supervisado** experimentan con un conjunto de datos que contiene muchas características, luego aprenden propiedades útiles de la estructura de este conjunto de datos. En el contexto del deep learning, generalmente se quiere aprender toda la distribución de probabilidad que generó un conjunto de datos, ya sea explícitamente como en la estimación de densidad o implícitamente para tareas como síntesis o eliminación de ruido.

- **Aprendizaje supervisado** experimentan con un conjunto de datos que contiene características, pero cada ejemplo también está asociado con una etiqueta o un objetivo.

## Function Loss o función de coste
La función de coste es una medida que se utiliza para evaluar el rendimiento de un modelo. Esta es una función matemática que calcula la diferencia entre las predicciones del modelo y los valores reales del conjunto de datos.

El objetivo del modelo es minimizar la función de coste para que pueda hacer predicciones precisas en los nuevos datos. El proceso de entrenamiento del modelo implica ajustar los parámetros del modelo para minimizar dicha función.

Existen diferentes tipos de funciones de coste y la elección de esta depende del tipo de problema que se está resolviendo y del modelo utilizado. Algunos ejemplos comunes son:

- **Error cuadrático medio (MSE):** común para problemas de regresión. Mide la diferencia entre las predicciones del modelo y los valores reales del conjunto de datos, elevando al cuadrado esta diferencia y tomando el promedio.

- **Entropía cruzada (CE):** común para problemas de clasificación. Mide la diferencia entre las probabilidades predichas por el modelo y las probabilidades reales de las clases, y toma el logaritmo de la probabilidad predicha.

- **Pérdida de bisagra (hinge loss):** común para problemas de clasificación binaria con soporte vectorial (SVM). Mide la discrepancia entre las predicciones del modelo y los valores reales del conjunto de datos, y se basa en la distancia entre los datos y el umbral de decisión del modelo.

- **Pérdida de Huber (Huber loss):** común para problemas de regresión. Es una combinación de la pérdida cuadrática y la pérdida absoluta, y se utiliza para reducir la sensibilidad del modelo a los valores atípicos (outliers)

## Hiperparámetros y conjunto de validación
Los hiperparámetros (hyperparameters) son variables ajustables que se utilizan para controlar el rendimiento y la capacidad de los algoritmos de machine learning. Estos se definen antes del entrenamiento del modelo y afectan directamente a este proceso y al resultado final del modelo.

El conjunto de validación (validation set) es una parte del conjunto de datos que se utiliza para evaluar el rendimiento del modelo durante el entrenamiento. 

El conjunto de validación se utiliza para ajustar los hiperparámetros del modelo y para evaluar su rendimiento en datos nuevos que no se utilizaron durante el entrenamiento.

### Cross Validation
La validación cruzada es una técnica que consiste en dividir el conjunto de datos en varios subconjuntos o "pliegues" y realizar múltiples iteraciones de entrenamiento y evaluación, en las que se utiliza un subconjunto diferente para la evaluación en cada iteración y los restantes para el entrenamiento del modelo. Esto permite aprovechar al máximo los datos disponibles para el entrenamiento y la evaluación, especialmente en conjuntos de datos pequeños, y proporciona una estimación más precisa.

Es una técnica comúnmente utilizada para la selección de modelos, la optimización de hiperparámetros y la evaluación del rendimiento.

## Capacity, Overfitting y Underfitting
Capacity, Overfitting y Underfitting son términos utilizados en machine learning para describir el rendimiento de un modelo en relación con los datos de entrenamiento y los datos de prueba.

- **Capacity (Capacidad):** se refiere a la capacidad del modelo para aprender la relación subyacente entre los datos de entrada y salida. Un modelo con baja capacidad puede no ser lo suficientemente complejo como para capturar la relación subyacente, mientras que un modelo con alta capacidad puede ser demasiado complejo y ajustarse demasiado a los datos de entrenamiento.

- **Overfitting (Sobreajuste):** ocurre cuando un modelo se ajusta demasiado a los datos de entrenamiento y pierde la capacidad de generalizar para nuevos datos. Es decir, el modelo ha aprendido a memorizar los datos de entrenamiento en lugar de aprender la relación subyacente.

- **Underfitting (Subajuste):** ocurre cuando un modelo no es lo suficientemente complejo como para capturar la relación subyacente entre los datos de entrada y salida. Como resultado, el modelo no puede ajustarse bien a los datos de entrenamiento y también tendrá un rendimiento pobre en los datos de prueba.

La **Dimensión de Vapnik-Chervonenkis (VC)** es una medida teórica que está relacionada con la capacidad modelo  para ajustarse a diferentes patrones en los datos. Por un lado, una alta dimensión VC significa que el modelo tiene una mayor capacidad para aprender relaciones complejas en los datos, lo que puede llevar a un sobreajuste de los datos de entrenamiento. Por otro lado, una baja dimensión VC puede llevar a un subajuste del modelo, ya que no es lo suficientemente complejo para capturar la relación subyacente en los datos. Por lo tanto, es importante tener en cuenta la dimensión VC al elegir un modelo y ajustar sus parámetros para evitar tanto el sobreajuste como el subajuste.

En resumen, encontrar un equilibrio adecuado entre la capacity del modelo y su capacidad para generalizar es fundamental para lograr un buen rendimiento. El objetivo es tener un modelo que sea lo suficientemente complejo como para capturar la relación subyacente, pero no tan complejo como para sobreajustar los datos de entrenamiento y perder la capacidad de generalizar para nuevos datos.

## Regularización
La regularización es una técnica que se utiliza para evitar el sobreajuste en un modelo. Esta implica agregar una penalización adicional a la función de coste del modelo que se está entrenando. Esta penalización se basa en los parámetros del modelo y puede tener diferentes formas. Por ejemplo:

- **La regularización L1:** también conocida como regularización Lasso, añade un término de penalización a la función objetivo que es proporcional al valor absoluto de los pesos del modelo. Esto tiene el efecto de llevar algunos de los pesos hacia cero, eliminándolos efectivamente del modelo y reduciendo su complejidad.

- **La regularización L2:** también conocida como regularización Ridge, añade un término de penalización a la función objetivo que es proporcional al cuadrado de los pesos del modelo. Esto tiene el efecto de empujar los pesos hacia cero, pero no hasta cero como en la regularización L1.

En ambos casos, el término de regularización es controlado por un hiperparámetro, comúnmente conocido como la fuerza de regularización o lambda ($\lambda$). Cuanto mayor sea el valor de lambda, más fuerte será el efecto de regularización y más complejo será el modelo. Encontrar el valor óptimo de lambda puede ser difícil y a menudo se hace mediante prueba y error o utilizando técnicas como la validación cruzada (cross-validation)

En resumen la regularización ayuda a reducir la complejidad del modelo, limitando la magnitud de los parámetros del modelo y, por lo tanto, evita que el modelo se ajuste demasiado bien a los datos de entrenamiento. Esto permite que el modelo generalice mejor a los datos nuevos y desconocidos.