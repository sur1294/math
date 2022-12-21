function [x, it] = newton_method(func, dfunc, x0, tol, maxit)
%newton_method: Use Newton method to find the root of a non-linear equation
%   Input:
%       func: given function
%       dfunc: derivative of the given function
%       x0: initial guess
%       tol: tolerance
%       maxit: maximum iterations
%   Output:
%       x: the root
%       it: number of iterations

% set initial values
x = x0;
it = 0;

% loop until converges or reaches the maximum number of iterations
while it < maxit
    % calculate the next approximation
    xnew = x - func(x)/dfunc(x);
    
    % check if we have converged
    if abs(x - xnew) < tol
        x = xnew;
        break;
    end
    
    % set new value of x
    x = xnew;
    it = it + 1;
end

if it == maxit
    disp('Reached maximum number of iterations!');
end

end