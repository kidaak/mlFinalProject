bigData = SongAnalysis.duration

bigData = [bigData SongAnalysis.end_of_fade_in];
bigData = [bigData double(SongAnalysis.key)]
bigData = [bigData SongAnalysis.loudness];
bigData = [bigData SongAnalysis.start_of_fade_out]
bigData = [bigData SongAnalysis.tempo];
bigData = [bigData double(SongAnalysis.time_signature)]

bigData = [bigData SongMetadata.artist_familiarity];
bigData = [bigData SongMetadata.artist_hotttnesss]
bigData = [bigData SongMetadata.song_hotttnesss];

%save('bigData','bigData');
