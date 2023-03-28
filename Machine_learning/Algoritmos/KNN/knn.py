import numpy as np

#KNN from scratch
class KNN:
    def __init__(self, k):
        self.k = k
        self.eps = 1e-8

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X_test):
        distances = self.compute_distance(X_test)
        return self.predict_labels(distances)

    def compute_distance(self, X_test):
        X_test_squared = np.sum(X_test ** 2, axis=1, keepdims=True)
        X_train_squared = np.sum(self.X_train ** 2, axis=1, keepdims=True)
        two_X_test_X_train = np.dot(X_test, self.X_train.T)

        # taking sqrt is not necessary: min distance won't change since sqrt is monotone)
        return np.sqrt(
            self.eps + X_test_squared - 2 * two_X_test_X_train + X_train_squared.T
        )

    def predict_labels(self, distances):
        num_test = distances.shape[0]
        y_pred = np.zeros(num_test)

        for i in range(num_test):
            y_indices = np.argsort(distances[i, :])
            k_closest_classes = self.y_train[y_indices[: self.k]].astype(int)
            y_pred[i] = np.argmax(np.bincount(k_closest_classes))

        return y_pred

# test KNN from scratch and implementation with sklearn
if __name__ == "__main__":
    from sklearn import datasets
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split

    # load dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # split dataset in train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=19
    )

    # implementation knn from scratch
    k = 3
    clf = KNN(k=k)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN from scratch classification accuracy", accuracy_score(y_test, predictions))

    # implemntation knn of sklearn
    from sklearn.neighbors import KNeighborsClassifier
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    print("KNN sklearn classification accuracy", accuracy_score(y_test, predictions))