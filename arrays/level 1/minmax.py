n=[1,23,43,12,22,1234]
#print(min(n))
#print(max(n))
minn=0
maxx=0
for i in n:
    if minn==0 and maxx==0:
        minn+=i
        maxx+=i
    if i<minn:
        minn=i
    if i>maxx:
        maxx=i
print(maxx)
print(minn)
    
