import scipy.sparse as sparse
import scipy.io as sio
import numpy as np

TYPEOFCLUSTERING = "KMeans"
LIMIT = 100

for clusters in range(2,50):
	data = np.zeros(shape=(LIMIT+1,clusters))
	inputFile = open('userClusterFeatureVectors/'+TYPEOFCLUSTERING+str(LIMIT)+"/"+str(clusters)+'clusters.csv', 'r')
	output = open('userClusterFeatureVectors/'+TYPEOFCLUSTERING+str(LIMIT)+"Normalized/"+str(clusters)+'clusters.csv', 'w')
	try:
		for line in inputFile:
			splitLine = line.split(',')
			user = int(splitLine[0])
			col = int(splitLine[1])
			count = float(splitLine[2])
			data[user,col] = count
		normData = data/np.max(np.abs(data),axis=0)
		for row in range(0,normData.shape[0]):
			for column in range(0,normData.shape[1]):
				output.write(str(row)+","+str(column)+","+str(normData[row,column])+"\n")
	finally:
		inputFile.close()
		output.close()