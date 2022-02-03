#finding the max area of binary  
#we will convert binary area matrix(i.e 2d matrix) we convert into 1d matrix by appending each row and calculating the max area of that area 




#function for max area of histogram
def mah(arr,n):
    right_stack=[]
    right_res=[]
    psudo_index=n+1
    
    for i in range(n-1,-1,-1):
        if len(right_stack)<0:
            right_res.append(psudo_index)
        elif len(right_stack)>0 and right_stack[-1][0]<arr[i]:
            right_res.append(right_stack[-1][1])
        elif len(right_stack)>0 and right_stack[-1][0]>=arr[i]:
            while len(right_stack)>0 and right_stack[-1][0]>=arr[i]:
                right_stack.pop(-1)
            if len(right_stack)==0:
                right_res.append(psudo_index)
            else:
                right_res.append(right_stack[-1][1])
                
        right_stack.append([arr[i],i])
        
    right_res=right_res[::-1]
    
    left_res=[]
    left_stack=[]
    
    for i in range(n):
        if len(left_stack)<0:
            left_stack.append(-1)
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
    #return left_res
        
    width=[]
    for i in range(len(right_res)):
        width.append(right_res[i]-left_res[i]-1)
    area=[]
    for i in range(len(width)):
        area.append(arr[i]*width[i])
        
    return max(area)
    

#print(mah([6,2,5,4,5,6],6))

res=[]
#extracting the 1st row of the matrix and appending to res

# m is len(row) and n is len(col)
# assuming arr is binary matrix containing n*m size
for j in range(m):
    res.append(arr[0][j])
#applying the above function here to get amx area
mx=mah(res)
#transversing the remaining rows
#if we found 0 at base we will make the entire sum 0
#becuase without base there is no area
#transversing from 1 because we done for the 0th row already
for i in range(1,n):
    for j in range(m):
        if arr[i][j]==0:
            res[j]=0
        else:
            res[j]+=arr[i][j]
#checking the max area for each appending row
mx1=max(mx,mah(res))
return mx1
#returning the max area
