import scipy.sparse as sparse
import scipy.io as sio
from sklearn import metrics
import numpy as np
from sklearn.decomposition import PCA

def main():
	f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalVectors.mat')

	full = np.nan_to_num(np.matrix(f['finalVectors']))
	full /= np.max(np.abs(full),axis=0)
	fullSplit = np.array_split(full, 360)

	print("Done Reading")
	mtx = fullSplit[0]

	pca = PCA(n_components=2)
	pca.fit(full)
	simple = pca.transform(full)
	#print(simple)
	print(pca.components_)
	print(pca.explained_variance_ratio_)

main()