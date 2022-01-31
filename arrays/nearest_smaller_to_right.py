
arr=[1,0,3,2,4]
stack=[]
n=len(arr)
res=[]
for i in range(n-1,-1,-1):
    if len(stack)==0:
        res.append(-1)
    elif len(stack)>0 and stack[-1]<arr[i]:
        res.append(stack[-1])
    elif len(stack)>0 and stack[-1]>=arr[i]:
        while len(stack)>0 and stack[-1]>=arr[i]:
            stack.pop(-1)
        if len(stack)==0:
            res.append(-1)
        else:
            stack.append(stack[-1])
    stack.append(arr[i])
res=res[::-1]
print(res)
