import scipy.sparse as sparse
import scipy.io as sio
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

def plot(mtx,labels):
	pca = PCA(n_components=3)
	pca.fit(mtx)
	print(pca.explained_variance_ratio_)
	simple = pca.transform(mtx)
	use_colours = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4:"cyan", 5:"magenta", 6:"black"}
	fig = pl.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(simple[:,0],simple[:,1], simple[:,2], c=[use_colours[x] for x in labels])
	pl.show()
def main():
	f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

	full = np.nan_to_num(np.matrix(f['finalVectors']))
	fullSplit = np.array_split(full, 36)

	print("Done Reading")
	mtx = fullSplit[0]
	print(len(mtx))
	mtx /= np.max(np.abs(mtx),axis=0)
	for clusters in range(2,25):
		errors = 0
		num_clusters = clusters
		ClusteringKmeans = MiniBatchKMeans(n_clusters=num_clusters)
		ClusteringKmeans.fit(mtx)
		result = ClusteringKmeans.labels_
		silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
		plot(mtx,result)
		print("Clusters:", clusters, "Silhouette Score:", silhouette, "Retest Error:", errors)

	# num_clusters = 3
	# ClusteringKmeans = MiniBatchKMeans(n_clusters=num_clusters)
	# ClusteringKmeans.fit(mtx)
	# result = ClusteringKmeans.labels_
	# silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')

	# readable = [0]*num_clusters
	# for x in range(0, len(result)):
	# 	readable[result[x]] += 1


	# print(readable)
	# print(silhouette)

main()