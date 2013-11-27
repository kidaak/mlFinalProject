import scipy.sparse as sparse
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA


LIMIT = 1000

f = open('userFeatureVectors.txt', 'r')
row = []
col = []
data = []


i=0
for line in f:
	if(i<LIMIT):
		lineArray = line.split(',(')
		for x in range(1,len(lineArray)):
			playTuple = lineArray[x].rstrip(')\n')
			playTupleArray = playTuple.split(',')
			row.append(i)
			col.append(int(playTupleArray[0]))
			data.append(int(playTupleArray[1]))
		i=i+1
	else:
		break

spRow = np.array(row)
spCol = np.array(col)
spData = np.array(data)
mtx = sparse.coo_matrix((spData,(spRow,spCol)))

print("Done Reading")

pca = PCA(n_components=3)
pca.fit(mtx.toarray())
print(pca.explained_variance_ratio_)

for clusters in range(2,50):
	num_clusters = clusters
	ClusteringKmeans = KMeans(n_clusters=num_clusters)
	ClusteringKmeans.fit(mtx)
	result = ClusteringKmeans.labels_
	silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
	print("Clusters:", clusters, "Silhouette Score:", silhouette)


#num_clusters = 97
#ClusteringKmeans = KMeans(n_clusters=num_clusters)
#ClusteringKmeans.fit(mtx)
#result = ClusteringKmeans.labels_

#readable = [0]*num_clusters
#for x in range(0, len(result)):
#	readable[result[x]] += 1


#print(readable)
