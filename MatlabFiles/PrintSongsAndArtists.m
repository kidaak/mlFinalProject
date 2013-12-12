load SPA.mat;
fileID = fopen('SongsAndArtists');
fprintf(fileID, '%s, %s, %s\n',SongsPlusArtistsFromIDs{:,:});
fclose(fileID);