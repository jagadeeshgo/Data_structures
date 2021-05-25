#moving all negative numbers to the front and positive to the end with constant extra space

input1=[-12, 11, -13, -5, 6, -7, 5, -3, -6]

print(sorted(input1))       #we can solve simply by sorting 



j=0                  #if you want to do without using any inbuilt function
for i in range(1,len(input1)):  #order is not needed
    if (input1[i]<0):
        temp=input1[i]
        input1[i]=input1[j]
        input1[j]=temp
        j=j+1
        
print(input1)
        
