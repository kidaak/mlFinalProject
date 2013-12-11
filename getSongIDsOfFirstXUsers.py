import scipy.sparse as sparse
import scipy.io as sio
from sklearn import metrics
import numpy as np

LIMIT = 500
userSongs = {}
songMap = {}
songPosition = {}

user = open('userFeatureVectors.txt', 'r')
try:
	counter = 0
	for line in user:
		if counter>LIMIT:
			break
		splitLine = line.split(',(')
		userSongs[splitLine[0]] = []
		for song in range(1,len(splitLine)):
			splitSong = splitLine[song][:-1].split(',')
			userSongs[splitLine[0]] += [[splitSong[0],splitSong[1]]]
		counter +=1
finally:
	user.close()

sMap = open('songIndexMap.txt','r')
try:
	for line in sMap:
		splitMap = line.split(',')
		songMap[int(splitMap[1])] = splitMap[0]
finally:
	sMap.close()

f= sio.loadmat('/home/dmitriy/workspace/MLFinalProject/MatlabFiles/finalSongIDs.mat')
f1= f['finalSongIDs']
for songID in range(0,f1.shape[0]):
	songPosition[f1[songID][0][0]] = songID

output = open('songIDsofFirst'+str(LIMIT)+'Users.txt','w')
try:
	for key in userSongs.keys():
		print userSongs[key]
		for songAndPlayCount in userSongs[key]:
			output.write(str(songPosition[songMap[int(songAndPlayCount[0])]])+"\n")
finally:
	output.close()