finalVectors = zeros(385256, 10);
x = uint64(1);
for i = 1:1000000,
    if(userSongIndices(i) == 1)
        finalVectors(x, :) = bigData(i,:);
        x = x+1
    end
end
save('finalVectors','finalVectors');