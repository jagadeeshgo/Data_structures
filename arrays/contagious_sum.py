
arr=[1,2,3,7,5]
i,j=0,0
sum1=0
s=12
while j<n:
  sum1+=arr[j]
  
  if sum1<s:
    j+=1
  elif sum1==s:
    print(i+1,j+1)
  else:
    while sum1>s:
      sum1-=arr[i]
      i+=1
      
    if sum1==s:
      print(i+1,j+1)
        
    j+=1
print('not available')
      

  
