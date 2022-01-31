arr=[6,2,5,4,5,1,6]
right_stack=[]
n=len(arr)
right_res=[]
right_psudo_index=7
for i in range(n-1,-1,-1):
    if len(right_stack)==0:
        right_res.append(right_psudo_index)
    elif len(right_stack)>0 and right_stack[-1][0]<arr[i]:
        right_res.append(right_stack[-1][1])
    elif len(right_stack)>0 and right_stack[-1][0]>=arr[i]:
        while len(right_stack)>0 and right_stack[-1][0]>=arr[i]:
            right_stack.pop(-1)
        if len(right_stack)==0:
            right_res.append(right_psudo_index)
        else:
            right_res.append(right_stack[-1][1])
    right_stack.append([arr[i],i])
right_res=right_res[::-1]

print(right_res)
##########

left_res=[]
left_stack=[]
for i in range(n):
    if len(left_stack)==0:
        left_res.append(-1)
        
    elif len(left_stack)>0 and left_stack[-1][0]<arr[i]:
        left_res.append(left_stack[-1][1])
    elif len(left_stack)>0 and left_stack[-1][0]>=arr[i]:
        while len(left_stack)>0 and left_stack[-1][0]>=arr[i]:
            left_stack.pop(-1)
        if len(left_stack)==0:
            left_res.append(-1)
        else:
            left_res.append(left_stack[-1][1])
    left_stack.append([arr[i],i])
print(left_res)
width=[]
for i in range(len(right_res)):
    #print(i)
    width.append(right_res[i]-left_res[i]-1)
print(width)
area=[]
for i in range(len(width)):
    area.append(arr[i]*width[i])
    
print(max(area))
    
