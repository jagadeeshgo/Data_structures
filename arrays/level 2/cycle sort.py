# cycle sort
#moving the last element to the 1st in a cyclic order

n=[1,2,3,4,5]  #here we should move 5 to 1st place

last_element=n[(len(n))-1]

size=len(n)

for i in range(size-1,0,-1):
    n[i]=n[i-1]
n[0]=last_element

print(n)
