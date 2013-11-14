import scipy.sparse as sparse
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import Ward


LIMIT = 1000000

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

num_clusters = 20
ClusteringKmeans = KMeans(n_clusters=num_clusters)
ClusteringKmeans.fit(mtx)
result = ClusteringKmeans.labels_

#ClusteringHier = Ward(n_clusters = num_clusters)
#result = ClusteringHier.fit_predict(mtx.toarray())


readable = [0]*num_clusters
for x in range(0, len(result)):
	readable[result[x]] += 1


print(readable)
