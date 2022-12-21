x = [1,2,3];  % given data points
y = [2,4,7];
n = length(x);  % number of data points

syms t;  % declaring the symbol t for general polynomial of degree n

L = 0;  % declaring the Lagrange polynomial

for i=1:n
    % Calculating the polynomial by taking the product of each factor
    temp = 1;
    for j=1:n
        if i~=j
            temp = temp*(t-x(j))/(x(i)-x(j));
        end
    end
    L = L + y(i)*temp;  % Adding the current factor to the polynomial
end

disp(L);  % Displaying the result