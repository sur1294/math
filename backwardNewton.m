function [x,err] = backwardNewton(f,x)
    % Set tolerance
    tol = 1e-6;
    % Initialize error
    err = 1;
    % Set max iterations
    maxiter = 1000;
    % Initialize iteration count
    iter = 0;

    while err > tol && iter <= maxiter
        % Evaluate f
        fx = f(x);
        % Evaluate derivative of f
        dfx = diff(f,x);
        % Update x
        x = x - fx/dfx;
        % Calculate error
        err = abs(f(x));
        % Iterate
        iter = iter + 1;
    end
    
    if iter > maxiter
        error('Maximum iteration limit reached');
    end
end