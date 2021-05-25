n=[15,16,10,9,6,7,17]

Range=max(n)-min(n)  #we can simply use in built function

coefficient_range=(max(n)-min(n))/(max(n)+min(n))

print(Range)
print(coefficient_range)



size=len(n)              #or we can make our own function
def getmin(n,size):
    result=n[0]
    for i in range(1,size):
        result=min(result,n[i])
    return result

def getmax(n,size):
    result=n[0]
    for i in range(1,size):
        result=max(result,n[i])
    return result

def findRangeandCoefficient(n,size):
    Range=getmax(n,size)-getmin(n,size)
    Coefficient=Range/(getmin(n,size)+getmax(n,size))

    return Range,Coefficient
    

print(findRangeandCoefficient(n,size))
    

