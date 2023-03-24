import numpy as np

class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.components = None
        self.mean = None

    def fit(self, X):
        # mean centering
        self.mean = np.mean(X, axis=0)
        X = X - self.mean

        # covariance, functions needs samples as columns
        cov = np.cov(X.T)

        # eigenvectors, eigenvalues
        eigenvectors, eigenvalues = np.linalg.eig(cov)

        # eigenvectors v = [:, i] column vector, transpose this for easier calculations
        eigenvectors = eigenvectors.T

        # sort eigenvectors
        idxs = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[idxs]
        eigenvectors = eigenvectors[idxs]

        self.components = eigenvectors[:self.n_components]

    def transform(self, X):
        # projects data
        X = X - self.mean
        return np.dot(X, self.components.T)
    
# test PCA from scratch and implementation with sklearn
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from sklearn import datasets

    # load dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # Project the data onto the 2 primary principal components with pca from scratch
    pca = PCA(2)
    pca.fit(X)
    X_projected = pca.transform(X)

    # Project the data onto the 2 primary principal components with pca of sklearn
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    X_projected_sk = pca.fit_transform(X)
    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('PCA')
    ax1.scatter(X_projected[:, 0], X_projected[:, 1], c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3))
    ax1.set_title("scratch")
    ax2.scatter(X_projected_sk[:, 1], X_projected_sk[:, 0], c=y, edgecolor="none", alpha=0.8, cmap=plt.cm.get_cmap("viridis", 3))
    ax2.set_title("sklearn")
    plt.show()

