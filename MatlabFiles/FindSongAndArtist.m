temp = cell(95, 2);
for i=1:95,
    for j=1:size(SongIDs),
        if(strcmp(neededSongs{i},SongIDs{j}) == 1)
            temp(i,:) = songArtist(j,:);
            break;
        end
    end
    if(mod(i,50) == 0)
        Completed = i
        
    end
end
%userSongIndicesPtC = temp;
%save('userSongIndicesPtC','userSongIndicesPtC');