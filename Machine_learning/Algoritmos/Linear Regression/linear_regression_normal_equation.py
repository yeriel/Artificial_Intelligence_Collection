'''Implementación de Regresión Lineal usando la Ecuación Normal.

Sea m = #ejemplos de entrenamiento, n = #número de características y las
formas de entrada son y es R^(m x 1), X es R^(m x n), w es R^(n x 1).
Usando estas formas, la implementación de la ecuación normal es
exactamente como la fórmula derivada :)'''

import numpy as np

def linear_regression_normal_equation(X, y):
    ones = np.ones((X.shape[0], 1))
    X = np.append(ones, X, axis=1)
    W = np.dot(np.linalg.pinv(np.dot(X.T, X)), np.dot(X.T, y))
    return W


if __name__ == "__main__":
    m, n = 500, 1
    X = np.random.rand(m, n)
    y = 5 * X + np.random.randn(m, n) * 0.1
    W = linear_regression_normal_equation(X, y)
    print(W)