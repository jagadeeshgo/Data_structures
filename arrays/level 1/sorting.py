n=[1,5,3,6]
#print(sorted(n))

out=[]
cur=0
temp=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp
            
print(n)
