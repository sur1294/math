function [x, nIter] = forwardNewton(f, x0, tol)
    nIter = 0;
    x = x0;
    while (1)
        nIter = nIter + 1;
        fx = f(x);
        if (norm(fx) <= tol)
            break;
        end
        Dfx = forwardDiff(f, x);
        x = x - Dfx \ fx;
    end
end
