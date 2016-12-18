function angleset = jangle(Ri, Rf, di,df, anglei, doordim)
    angleset = [];
    posi = [di(1) - Ri(1);di(2) - Ri(2);1];
    posf = [df(1) - Rf(1); df(2) - Rf(2);1];
    delx = posf - posi;
    while norm([delx(1),delx(2)])> 0.01
        J = getjacobian(anglei(1), anglei(2),doordim);
        invJ = pinv(J);
        delAngle = invJ*delx;
        
        anglen = anglei + 0.1*delAngle;
       
        angleset = [angleset,anglen];
        pos = forward(anglen(1),anglen(2),doordim);
        delx = posf - pos;
        anglei = anglen;
       
    end
end

function j = getjacobian(theta, phi, d)
    j = [ -(d*(sin(phi + theta) + sin(theta)))/2, -(d*sin(phi + theta))/2;...
  (d*(cos(phi + theta) + cos(theta)))/2,  (d*cos(phi + theta))/2;...
                                      0,                       0];
                              
end
function X = forward(theta, phi,d)
    
 X =  [(d*(cos(phi)*cos(theta) - sin(phi)*sin(theta)))/2 + (d*cos(theta))/2;...
 (d*(cos(phi)*sin(theta) + cos(theta)*sin(phi)))/2 + (d*sin(theta))/2;...
                                                                    1];
end