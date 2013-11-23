temp = zeros(15000, 1);
for i=505001:520000,
    for j=1:size(userSongIDs),
        if(strcmp(SongIDs{i},userSongIDs{j}) == 1)
            temp(i-505000,1) = 1;
            break;
        end
    end
    if(mod(i,50) == 0)
        Completed = i
        
    end
end
userSongIndicesPtC = temp;
save('userSongIndicesPtC','userSongIndicesPtC');