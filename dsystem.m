syms x(t) y(t) z(t)
A = [1 2 -1; 0 1 0;0 0 1];
Y = [x; y;z];
odes = diff(Y) == A*Y 
[xSol(t),ySol(t),zSol(t)] = dsolve(odes);
xSol(t) = simplify(xSol(t))
ySol(t) = simplify(ySol(t))
zSol(t) = simplify(zSol(t))