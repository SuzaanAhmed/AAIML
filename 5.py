import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load IRIS dataset
iris = load_iris()
X = iris.data            
y = iris.target          

# Number of clusters for iris = 3
k = 3

# K-Means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

kmeans_sil = silhouette_score(X, kmeans_labels)

print("K-Means Clustering")
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("Silhouette Score:", kmeans_sil)
print("----------------------------------")

# EM (Gaussian Mixture)
gmm = GaussianMixture(n_components=k, random_state=42)
gmm_labels = gmm.fit_predict(X)

gmm_sil = silhouette_score(X, gmm_labels)

print("EM (Gaussian Mixture) Clustering")
print("Means:\n", gmm.means_)
print("Silhouette Score:", gmm_sil)
print("----------------------------------")

# Comparison
print("Comparison:")
print(f"K-Means Silhouette Score: {kmeans_sil:.4f}")
print(f"EM (GMM) Silhouette Score: {gmm_sil:.4f}")

if gmm_sil > kmeans_sil:
    print("→ EM (GMM) produced better clusters.")
else:
    print("→ K-Means produced better clusters.")

# Visualize (first two features)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels, cmap='viridis')
plt.title("K-Means Clustering (Iris)")

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=gmm_labels, cmap='viridis')
plt.title("EM (GMM) Clustering (Iris)")

plt.show()