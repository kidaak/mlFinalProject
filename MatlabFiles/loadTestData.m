SongAnalysis = h5read('subset_msd_summary_file.h5', '/analysis/songs/');
SongMetadata = h5read('subset_msd_summary_file.h5', '/metadata/songs/');

songIDs = SongMetadata.song_id;
songIDs = transpose(songIDs);
songIDs = cellstr(songIDs)

makeBigData;

load('userSongIDs');