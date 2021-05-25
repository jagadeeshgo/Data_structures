n=[1,2,4,4,5,5,5]
count=0
out=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            
            out.append(n[i])
print(set(out))


k=5
count1=0
for i in n:
    if i==k:count1+=1
print(count1)
