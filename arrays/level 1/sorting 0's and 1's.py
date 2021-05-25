a=[0,0,2,1,1,1,0,0,1]

#print(sorted(n))

#assuming mid and lo is 0
mid=0
high=len(a)-1
lo=0

while mid<=high:
    
    if a[mid]==0:  #0 should not be in mid position 
        a[lo],a[mid]=a[mid],a[lo]
        lo+=1
        mid+=1
        
    elif a[mid]==1: #1 can be in mid
        mid=mid+1
        
    else:
        a[mid],a[high]=a[high],a[mid] #2 should be in hi position
        high=high-1
        
print(a)
