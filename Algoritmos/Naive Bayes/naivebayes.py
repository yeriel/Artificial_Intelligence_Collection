import numpy as np

class NaiveBayes:
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # calculate mean, var, and prior for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)

        for idx, c in enumerate(self._classes):
            X_c = X[y == c]
            self._mean[idx, :] = X_c.mean(axis=0)
            self._var[idx, :] = X_c.var(axis=0)
            self._priors[idx] = X_c.shape[0] / float(n_samples)

    def predict(self, X):
        return np.array([self._predict(x) for x in X])

    def _predict(self, x):
        # calculate posterior probability for each class
        # prior + posterior
        posteriors = [np.log(self._priors[idx]) + np.sum(np.log(self._pdf(idx, x))) for idx, _ in enumerate(self._classes)]

        # return class with highest posterior probability
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        return (np.exp(-((x - mean) ** 2) / (2 * var))) / (np.sqrt(2 * np.pi * var))

# test GNB from scratch and implementation with sklearn
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

    # implementation GNB from scratch
    nb = NaiveBayes()
    nb.fit(X_train, y_train)
    predictions = nb.predict(X_test)
    print("Naive Bayes classification from scratch accuracy", accuracy_score(y_test, predictions))

    # implementation knn of sklearn
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    predictions = gnb.predict(X_test)
    print("Naive Bayes classification of sklearn accuracy", accuracy_score(y_test, predictions))
