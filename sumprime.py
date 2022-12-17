def sumprimes(l):
 sum=0
 for i in range(len(l)):
      n=l[i]
      j=0
      if n>1:
       for i in range(2,n):
          if n%i==0:
           j=j+1
       if j==0:
        sum=sum+n
 return(sum)
      