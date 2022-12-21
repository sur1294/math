%Define A 
A = [3 -2 4; 5 7 -6; 2 0 -3];

%Define b 
b = [12; -25; 6];

%Define n 
n = length(b);

%Initialize L, U, and x
L = eye(n);
U = A;
x = zeros(n,1);

%Gauss Elimination 
for k = 1 : n-1
    for i = k+1 : n
        L(i,k) = U(i,k)/U(k,k);
        U(i,:) = U(i,:) - L(i,k)*U(k,:);
        b(i) = b(i) - L(i,k)*b(k);
    end
end

%Forward Substitution 
for k = 1 : n
    x(k) = b(k);
    for j = 1 : k-1
        x(k) = x(k) - L(k,j)*x(j);
    end
    x(k) = x(k)/L(k,k);
end

%Back Substitution 
for k = n : -1 : 1
    x(k) = b(k);
    for j = k+1 : n
        x(k) = x(k) - U(k,j)*x(j);
    end
    x(k) = x(k)/U(k,k);
end

%Display Results 
disp('L =');
disp(L);
disp('U =');
disp(U);
disp('x =');
disp(x);