import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)

print(f'coeficientes {reg.coef_}') 
print(f'intercepto {reg.intercept_}')
print(f'prediccion para (3,5) {reg.predict(np.array([[3, 5]]))}')
