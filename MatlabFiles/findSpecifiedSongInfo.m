%SongMetadata = h5read('msd_summary_file.h5', '/metadata/songs/');

%songArtist = cellstr(transpose(SongMetadata.title));

%songArtist = [songArtist cellstr(transpose(SongMetadata.artist_name))];

%save('songArtist','songArtist');

%fileID = fopen('newSongIDs');
%A = textscan(fileID, '%s');
%neededSongs = A{1,1};

load songArtist.mat;
load neededSongs.mat;