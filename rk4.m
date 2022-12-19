​h=0.1;
t=0:0.1:10;
n=(10/0.1);
x(1)=8;
y(1)=3;
for i=1:n
   a=x(i);
   b=y(i);
    k1=h*(2*a-3*b);
    l1=h*(b-2*a);
    k2=h*(2*(a+(k1/2))-3*(b+(l1/2)));
    l2=h*((b+(l1/2))-2*(a+(k1/2)));
    k3=h*(2*(a+(k2/2))-3*(b+(l2/2)));
    l3=h*((b+(l2/2))-2*(a+(k2/2)));
     k4=h*(2*(a+k3)-3*(b+l3));
    l4=h*((b+l3)-2*(a+k3));

    k=(k1+2*k2+2*k3+k4)/6;
    l=(l1+2*l2+2*l3+l4)/6;
    x(i+1)=x(i)+k;
    y(i+1)=y(i)+l;
end
for i=1:n+1
    xr(i)=5*exp(-t(i))+3*exp(4*t(i));
     yr(i)=5*exp(-t(i))-2*exp(4*t(i));
end
%comparison
disp(' value of x(10) using RK4')
x(n+1)
disp(' value of y(10) using RK4')
y(n+1)
disp(' value of x(10) using rigrous solution')
xr(n+1)
disp(' value of y(10) using rigrous solution')
yr(n+1)
disp('relative error in x(10)')
ex=abs((x(n+1)-xr(n+1))/x(n+1))
disp('relative error in y(10)')
ey=abs((y(n+1)-yr(n+1))/y(n+1))

​