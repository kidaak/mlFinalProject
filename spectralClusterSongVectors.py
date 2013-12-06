import scipy.sparse as sparse
import scipy.io as sio
from sklearn import metrics
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as pl
from sklearn.cluster import SpectralClustering
from mpl_toolkits.mplot3d import Axes3D
import itertools

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
	f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

	full = np.nan_to_num(np.matrix(f['finalVectors']))
	fullSplit = np.array_split(full, 360)

	print("Done Reading")
	mtx = fullSplit[0]
	mtx /= np.max(np.abs(mtx),axis=0)
	print np.ptp(mtx, axis=0)
	i=0
	for i in range(19,20):
		num_clusters=i
		spectral = SpectralClustering(n_clusters=num_clusters, affinity="rbf")
		spectral.fit(mtx)
		result = spectral.labels_
		silhouette = metrics.silhouette_score(mtx,result,metric='euclidean')
		readable = [0]*num_clusters
		plot(mtx, result)
		#for x in range(0, len(result)):
		#	readable[result[x]] += 1


		#print(readable)
		#print(i,silhouette)

main()
