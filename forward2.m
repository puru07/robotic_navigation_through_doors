function X = forward2(angle,d)
theta = angle(1);
phi = angle(2);
  X = zeros(3,2);  
 X(:,2) =  [(d*(cos(phi)*cos(theta) - sin(phi)*sin(theta)))/2 + (d*cos(theta))/2;...
 (d*(cos(phi)*sin(theta) + cos(theta)*sin(phi)))/2 + (d*sin(theta))/2;...
                                                                    1];
X(:,1) = [(d/2)*cos(theta);(d/2)*sin(theta);1];
end