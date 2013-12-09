import scipy.sparse as sparse
import scipy.io as sio
from sklearn import metrics
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as pl
from sklearn.cluster import SpectralClustering
from mpl_toolkits.mplot3d import Axes3D
import itertools

songIDsToCluster = []

def plot(mtx,labels):
	pca = PCA(n_components=3)
	pca.fit(mtx)
	print(pca.explained_variance_ratio_)
	simple = pca.transform(mtx)
	color_iter = itertools.cycle(['r', 'g', 'b', 'c', 'm'])
	fig = pl.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(simple[:,0],simple[:,1], simple[:,2], c=[color for color in color_iter])
	pl.show()

def main():
	songIds = open("songIDsofFirst100Users.txt","r")
	try:
		for line in songIds:
			songIDsToCluster.append(int(line))
	finally:
		songIds.close()

	f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

	full = np.nan_to_num(np.matrix(f['finalVectors']))
	# print full.shape
	# fullSplit = np.array_split(full, 20)

	# print("Done Reading")
	# #for partition in range(0,len(fullSplit))
	# mtx = fullSplit[0]

	mtx = full[songIDsToCluster]
	print mtx.shape

	mtx /= np.max(np.abs(mtx),axis=0)
	print np.ptp(mtx, axis=0)
	i=0
	for i in range(3,25):
		num_clusters=i
		spectral = SpectralClustering(n_clusters=num_clusters, affinity="rbf")
		spectral.fit(mtx)
		result = spectral.labels_
		writeSongIDandClusterToFile(result,i)
		#silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
		#readable = [0]*num_clusters
		#plot(mtx, result)
		#for x in range(0, len(result)):
		#	readable[result[x]] += 1


		#print(readable)
		#print(i,silhouette)	finally:

def writeSongIDandClusterToFile(results,clusters):
	o= open('james_songIDandCluster/'+str(clusters)+"clusters.csv", 'w')
	try:
		for i in range(0,len(results)):
			o.write(str(songIDsToCluster[i]) + "," + str(results[i])+"\n")
	finally:
		o.close()
	print "Finished " + str(clusters)

main()
