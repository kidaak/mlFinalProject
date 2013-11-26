import scipy.sparse as sparse
import scipy.io as sio
from sklearn import metrics
import numpy as np
from sklearn.cluster import SpectralClustering

f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

full = np.nan_to_num(np.matrix(f['finalVectors']))
fullSplit = np.array_split(full, 360)

print("Done Reading")
mtx = fullSplit[0]

i=0
for i in range(2,25):
	num_clusters=i
	spectral = SpectralClustering(n_clusters=num_clusters, affinity="nearest_neighbors")
	spectral.fit(mtx)
	result = spectral.labels_
	silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
	spectral2 = SpectralClustering(n_clusters=num_clusters, affinity="nearest_neighbors")
	spectral.fit(mtx)
	result2 = spectral.labels_
	errors = 0
	for j in range(0, len(result)):
 			if result[j]!=result2[j]:
 				errors += 1
 	print errors
	readable = [0]*num_clusters
	readable2 = [0]*num_clusters
	for x in range(0, len(result)):
		readable[result[x]] += 1
		readable2[result2[x]] += 1


	print(readable)
	print(readable2)
	#print(silhouette)
