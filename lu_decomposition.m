function [lower,upper] = lu_decomposition(A)
    n = size(A,1);
    lower = eye(n);
    upper = A;
    for i=1:n
        for j=i+1:n
            lower(j,i) = upper(j,i)/upper(i,i);
            for k=i:n
                upper(j,k) = upper(j,k)-lower(j,i)*upper(i,k);
            end
        end
    end
end