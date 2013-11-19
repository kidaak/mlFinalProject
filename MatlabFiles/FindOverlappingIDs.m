temp = zeros(500000, 1);
for i=1:500000,
    for j=1:size(userSongIDs),
        if(strcmp(songIDs{i},userSongIDs{j}) == 1)
            temp(i,1) = 1;
            break;
        end
    end
    if(mod(i,50) == 0)
        Completed = i
        
    end
end
userSongIndicesPt1 = temp;
save('userSongIndicesPt1','userSongIndicesPt1');