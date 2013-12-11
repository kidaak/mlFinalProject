import itertools
import scipy.sparse as sparse
import scipy.io as sio
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
import matplotlib as mpl
import matplotlib.pyplot as pl
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn import mixture
from scipy import linalg

songIDsToCluster = []

def main():
	bic = [0]*100
	clusters = [0]*100
	#for j in range(0,10):
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
	mtx = full[songIDsToCluster]
	mtx /= np.max(np.abs(mtx),axis=0)

	for i in range(25, 50):
		# pca = PCA(n_components=2)
		# pca.fit(mtx)
		# print(pca.explained_variance_ratio_)
		# simple = pca.transform(mtx)
		
		g = mixture.GMM(n_components=i)
		# Generate random observations with two modes centered on 0
		# and 10 to use for training.
		g.fit(mtx)
		#print(i, g.bic(mtx))
		clusters[i-2] = i
		bic[i-2] += g.bic(mtx)
		Y_ = g.predict(mtx)
		writeSongIDandClusterToFile(Y_,i)
		#graph(g,mtx)
	#pl.scatter(clusters,[e/50 for e in bic])
	pl.scatter(clusters,bic)
	#pl.show()
	#graph(g,mtx)
	#print g.weights_

def graph(gmm, X):
	#color_iter = itertools.cycle(['r', 'g', 'b', 'c', 'm'])
	#splot = pl.subplot(2, 1, 1)
	#Y_ = gmm.predict(X)

	#print Y_
	plot(X, Y_)

	# for i, (mean, covar, color) in enumerate(zip(gmm.means_, gmm._get_covars(), color_iter)):
	# 	v, w = linalg.eigh(covar)
	# 	u = w[0] / linalg.norm(w[0])
 #        # as the DP will not use every component it has access to
 #        # unless it needs it, we shouldn't plot the redundant
 #        # components.
	# 	if not np.any(Y_ == i):
	# 		continue
	# 	pl.scatter(X[Y_ == i, 0], X[Y_ == i, 1], .8, color=color)

 #        # Plot an ellipse to show the Gaussian component
	# 	angle = np.arctan(u[1] / u[0])
	# 	angle = 180 * angle / np.pi  # convert to degrees
	# 	ell = mpl.patches.Ellipse(mean, v[0], v[1], 180 + angle, color=color)
	# 	ell.set_clip_box(splot.bbox)
	# 	ell.set_alpha(0.5)
	# 	splot.add_artist(ell)
	# pl.show()

def plot(mtx,labels):
	pca = PCA(n_components=3)
	pca.fit(mtx)
	print(pca.explained_variance_ratio_)
	simple = pca.transform(mtx)
	#color_iter = itertools.cycle(['r', 'g', 'b', 'c', 'm'])
	color_iter = ['r','g','b','c','m']
	fig = pl.figure()
	#ax = fig.add_subplot(111, projection='3d')
	ax = fig.add_subplot(111)
	#ax.scatter(simple[:,0],simple[:,1], simple[:,2], c=[color_iter[x%5] for x in labels])
	ax.scatter(simple[:,0],simple[:,1], c=[color_iter[x%5] for x in labels])
	pl.show()

def writeSongIDandClusterToFile(results,clusters):
	o= open('james_songIDandCluster/gmm100/'+str(clusters)+"clusters.csv", 'w')
	try:
		for i in range(0,len(results)):
			o.write(str(songIDsToCluster[i]) + "," + str(results[i])+"\n")
	finally:
		o.close()
	print "Finished " + str(clusters)


main()