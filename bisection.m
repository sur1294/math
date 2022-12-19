%BISECTION METHOD
t=1;
while t>0
in=input('enter initial interval')
a=in(1);
b=in(2);
fa=a*cosh(50/a)-a-10;
fb=b*cosh(50/b)-b-10;
t=fa*fb;
if t>0
    disp('wrong input');
end
end
tol=input('enter tolerance ');
e=tol+1;
while e>tol
    c=(a+b)/2;
    fc=c*cosh(50/c)-c-10;
    if fa*fc<0
        b=c;
    elseif fb*fc<0
        a=c;
    else
        e=0;
    end
    e=abs(a-b);
end
disp('root of given function by bisection is=')
disp(c)









    









