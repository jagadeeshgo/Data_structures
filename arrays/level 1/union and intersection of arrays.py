#union and intersection of arrays

n1=[1, 3, 4, 5, 7]
n2=[2, 3, 5, 6]

union=sorted(n1+n2)
print(set(union))


intersection=[]
if (len(n1)>len(n2)):
    for i in n1:
        for j in n2:
            if i==j:
                intersection.append(i)
print(intersection)
    
        
