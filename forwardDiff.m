function Dfx = forwardDiff(f, x)
    h = 10^(-6);
    Dfx = zeros(length(x));
    for i = 1:length(x)
        x1 = x;
        x2 = x;
        x1(i) = x1(i) - h;
        x2(i) = x2(i) + h;
        Dfx(:, i) = (f(x2) - f(x1)) ./ (2*h);
    end
end