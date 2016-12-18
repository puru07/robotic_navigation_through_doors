function angle = doorangle(tree,robodim)
d =  tree(3);
h = tree(4);
v = tree(5);
if (d== 0) 
    corner = [tree(1)-robodim(1)/2,tree(2) + robodim(2)/2];
    angle = atan2(corner(2),corner(1));
elseif (d==2)
    angle = atan2(tree(2),tree(1));
else 
    corner = [tree(1)+ robodim(2)/2, tree(2) - robodim(1)/2];
    angle = atan2(corner(2),corner(1));
    
end