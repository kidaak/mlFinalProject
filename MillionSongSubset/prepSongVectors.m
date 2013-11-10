a = h5read('subset_msd_summary_file.h5', '/analysis/songs/');
b = h5read('subset_msd_summary_file.h5', '/metadata/songs/');

final = a.duration;
final = [final double(a.key)];
final = [final a.loudness];
final = [final a.tempo];
final = [final double(a.time_signature)];
final = [final b.artist_hotttnesss];
final = [final b.song_hotttnesss];

final