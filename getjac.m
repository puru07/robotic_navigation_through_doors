%figuring out the jac

syms theta phi d
vec = [d/2;0;1];
rtheta = [cos(theta),-1*sin(theta),0;...
            sin(theta), cos(theta), 0;...
            0, 0, 1];
rphi = [cos(phi),-1*sin(phi),0;...
            sin(phi), cos(phi), 0;...
            0, 0, 1];
trans = [1,0,d/2;0,1,0;0,0,1];
finalvec = rtheta*trans*rphi*vec
jac = jacobian(finalvec,[theta, phi]);
jac = simplify(jac)