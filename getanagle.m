function angleset = getanagle(Ri, Rf, di,df, anglei, doordim)
    global d;
    global Xf; 
    d = doordim;    
    angleset = [];
    posi = [di(1) - Ri(1);di(2) - Ri(2);1];
    posf = [df(1) - Rf(1); df(2) - Rf(2);1];
    Xf = posf;
    lb = [pi/2, -2*pi];
    ub = [2*pi,2*pi];
    angleset = fmincon(@tomin, anglei,[],[],[],[],lb,[],@nonl);

    
end
function [c,ceq] = nonl(angCurr)
    global d
    c = (d/2)*cos(angCurr(1));
    ceq = 0;
end
function out = tomin(angCurr)
    global d
    global Xf
    XC = forward(angCurr, d);
    err = XC- Xf;
    out  = norm(err);
end

function X = forward(angle,d)

theta = angle(1);
phi = angle(2);

 X =  [(d*(cos(phi)*cos(theta) - sin(phi)*sin(theta)))/2 + (d*cos(theta))/2;...
 (d*(cos(phi)*sin(theta) + cos(theta)*sin(phi)))/2 + (d*sin(theta))/2;...
                                                                    1];
end