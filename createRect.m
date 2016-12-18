function rectout = createRect(center, dim, fig)
figure(fig)
w = dim(1);
len = dim(2);
pos = [center(1) - w/2, center(2) + - len/2, w, len];
rectout = rectangle('Position', pos);   


end