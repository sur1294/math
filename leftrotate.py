def leftrotate(l):
    n=len(l)
    ln=[]
    for i in range(n):
      lk=[]
      for j in range(n):
        lk=lk+[l[j][n-i-1]]
      ln.append(lk)  
   
    return(ln)