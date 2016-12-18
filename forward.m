function X = forward(angle,d)
theta = angle(1);
phi = angle(2);
    
 X = [d*(cos(phi)*cos(theta) - sin(phi)*sin(theta)) + d*cos(theta); ...
 d*(cos(phi)*sin(theta) + cos(theta)*sin(phi)) + d*sin(theta);...
                                                            1];
end