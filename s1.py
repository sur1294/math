def intreverse(n):
 if n<=0:
  print('wrong input')
 else:
  l=[]
  while n!=0:
   e=n%10
   l=l+[e]
   n=n//10
  for i in range(0,len(l)):
   n=n+l[i]*pow(10,len(l)-1-i)

 return(n)
