import scipy.sparse as sparse
import scipy.io as sio
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

songIDsToCluster = []

def plot(mtx,labels):
	pca = PCA(n_components=3)
	pca.fit(mtx)
	print(pca.explained_variance_ratio_)
	simple = pca.transform(mtx)
	use_colours = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4:"cyan", 5:"magenta", 6:"black"}
	fig = pl.figure()
	#ax = fig.add_subplot(111, projection='3d')
	ax = fig.add_subplot(111)
	#ax.scatter(simple[:,0],simple[:,1], simple[:,2], c=[use_colours[x] for x in labels])
	ax.scatter(simple[:,0],simple[:,1], c=[use_colours[x%7] for x in labels])
	pl.title("KMeans")
	pl.show()
def main():
	songIds = open("songIDsofFirst100Users.txt","r")
	try:
		for line in songIds:
			songIDsToCluster.append(int(line))
	finally:
		songIds.close()
	print len(songIDsToCluster)

	f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

	full = np.nan_to_num(np.matrix(f['finalVectors']))
	# fullSplit = np.array_split(full, 360)

	# print("Done Reading")
	# mtx = fullSplit[0]
	# print(len(mtx))
	mtx = full[songIDsToCluster]
	mtx /= np.max(np.abs(mtx),axis=0)
	for clusters in range(25,50):
		errors = 0
		num_clusters = clusters
		ClusteringKmeans = KMeans(n_clusters=num_clusters)
		ClusteringKmeans.fit(mtx)
		result = ClusteringKmeans.labels_
		#silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
		#plot(mtx,result)
		writeSongIDandClusterToFile(result,clusters)
		print("Clusters:", clusters, "Retest Error:", errors)

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

def writeSongIDandClusterToFile(results,clusters):
	o= open('james_songIDandCluster/KMeans100/'+str(clusters)+"clusters.csv", 'w')
	try:
		for i in range(0,len(results)):
			o.write(str(songIDsToCluster[i]) + "," + str(results[i])+"\n")
	finally:
		o.close()
	print "Finished " + str(clusters)

main()