#searching the highest element in the right sub array if not found return -1
arr=[1,0,3,2,4]
stack=[]
#using the stack based approach
n=len(arr)
res=[]
#transversing the elements from backwards of the array
for i in range(n-1,-1,-1):
    if len(stack)==0:
        res.append(-1)
    elif len(stack)>0 and stack[-1]>arr[i]:
        res.append(stack[-1])
    elif len(stack)>0 and stack[-1]<=arr[i]:
        while len(stack)>0 and stack[-1]<=arr[i]:
            stack.pop(-1)
        if len(stack)==0:
            res.append(-1)
        else:
            res.append(stack[-1])
    stack.append(arr[i])
#while we came from back our output will be in reverse order
res=res[::-1]
print(res)
#time complexity O(n)
