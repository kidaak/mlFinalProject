%ECHONEST USERS
fileID = fopen('songIndexMap.txt');
A =  textscan(fileID,'%s %s', 'delimiter',',','EmptyValue',-Inf);
fclose(fileID);

%SONG ID
B = A{1}
%SONG INDEXES
C = A{2}


%MSD DATA
X = h5read('msd_summary_file.h5', '/analysis/songs/');
Y = h5read('msd_summary_file.h5', '/metadata/songs/');

%INITIAL SONG IDS
Z = Y.song_id

J = transpose(Z)
%FORMATTED SONG IDS
K = cellstr(J)