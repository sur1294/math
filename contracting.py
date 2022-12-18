def contracting(l):
   t=0
   for i in range(len(l)-2):
       if abs(l[i]-l[i+1])>abs(l[i+1]-l[i+2]):
         t=t+1
   if t==len(l)-2:
       return(True)
   else:
       return(False)