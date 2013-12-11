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
	print mtx.shape
	simple = pca.transform(mtx)
	print "Done Transforming"
	use_colours = {0: "red", 1: "green", 2: "blue", 3: "yellow", 4:"cyan", 5:"magenta", 6:"black"}
	fig = pl.figure()
	#ax = fig.add_subplot(111, projection='3d')
	ax = fig.add_subplot(111)
	#ax.scatter(simple[:,0],simple[:,1], simple[:,2], c=[use_colours[x] for x in labels])
	ax.scatter(simple[:,0],simple[:,1], c=[use_colours[x%7] for x in labels])
	pl.title("Spectral")
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
	#fullSplit = np.array_split(full, 360)

	#for partition in range(0,len(fullSplit))
	#mtx = fullSplit[0]

	mtx = full[songIDsToCluster]
	#print mtx.shape

	mtx /= np.max(np.abs(mtx),axis=0)
	#print np.ptp(mtx, axis=0)
	print("Done Reading")
	for i in range(25,50):
		num_clusters=i
		spectral = SpectralClustering(n_clusters=num_clusters, affinity="rbf")
		spectral.fit(mtx)
		result = spectral.labels_
		writeSongIDandClusterToFile(result,i)
		#silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
		#readable = [0]*num_clusters
		print "Done Clustering"
		#plot(mtx, result)
		#for x in range(0, len(result)):
		#	readable[result[x]] += 1


		#print(readable)
		#print(i,silhouette)	finally:

def writeSongIDandClusterToFile(results,clusters):
	o= open('james_songIDandCluster/spectral100/'+str(clusters)+"clusters.csv", 'w')
	try:
		for i in range(0,len(results)):
			o.write(str(songIDsToCluster[i]) + "," + str(results[i])+"\n")
	finally:
		o.close()
	print "Finished " + str(clusters)

main()
