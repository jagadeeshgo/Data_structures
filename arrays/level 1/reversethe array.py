n=[1,2,3,4]
#print(n[::-1])

out=[]
for i in range(0,len(n)):
    out.append((n[(len(n)-1)-i]))
print(out)
