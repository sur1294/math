def matched(s):
    l=len(s)
    m=[]
    for i in range(0,l):
        if s[i]=='(':
         m=m+[s[i]]
        elif s[i]==')':
         m=m+[s[i]]
    if len(m)%2!=0:
     return('False')
    else:
     j=0
     i=0
     while j>=0 and i<len(m):
      if m[i]=='(':
          j=j+1
      else:
          j=j-1
      i=i+1
     
     if j==0:
         return('True')
     else:
          return('False')
      
