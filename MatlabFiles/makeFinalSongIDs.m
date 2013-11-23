finalSongIDs = cell(385256, 1);
x = uint64(1);
for i = 1:1000000,
    if(userSongIndices(i) == 1)
        finalSongIDs(x) = SongIDs(i);
        x = x+1
    end
end
save('finalSongIDs','finalSongIDs');