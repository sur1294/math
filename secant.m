% secant method
% f(x)=sin(x)+cos(x)
a=0;
b=pi;
e=10^(-10);
t=1;
fa=sin(a)+cos(a);
fb=sin(b)+cos(b);
while t>e
    c=(a*fb-b*fa)/(fb-fa)
    fc=sin(c)+cos(c);
    t=abs(a-b);
    a=b;
    b=c;
    fa=fb;
    fb=fc;
end
disp('root is')
disp(c)

    
