import scipy.sparse as sparse
import scipy.io as sio
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances

f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

full = np.nan_to_num(np.matrix(f['finalVectors']))
fullSplit = np.array_split(full, 36)

print("Done Reading")
mtx = fullSplit[0]
print(len(mtx))
for clusters in range(2,25):
	errors = 0
	num_clusters = clusters
	ClusteringKmeans = MiniBatchKMeans(n_clusters=num_clusters)
	ClusteringKmeans.fit(mtx)
	result = ClusteringKmeans.labels_
	silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
	ClusteringKmeans2 = MiniBatchKMeans(n_clusters=num_clusters)
	ClusteringKmeans2.fit(mtx)
	result2 = ClusteringKmeans2.labels_
	for i in range(0, len(result)):
		if result[i]!=result2[i]:
			errors += 1
	readable = [0]*num_clusters
	readable2 = [0]*num_clusters
	for x in range(0, len(result)):
	 	readable[result[x]] += 1
	 	readable2[result2[x]] += 1
	#print("Clusters:", clusters, "Silhouette Score:", silhouette, "Retest Error:", errors)
	print(readable)
	print(readable2)

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