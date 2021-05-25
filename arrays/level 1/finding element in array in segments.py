arr=[1,2,3,4,5,3,7,8,3]
k=3
m=3
count=0
out=0
for i in arr:
    count+=1
        
    if i==k and count % m ==0:
        out+=1
    
if out!=0:
    print('yes')
else:
    print('no')
     


        
    
