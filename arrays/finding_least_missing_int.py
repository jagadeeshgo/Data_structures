
#using the index of each element
  def missingNumber(self,arr,n):
        
        for i in range(n):
            correct_pos=arr[i]-1
            
            while 1<=arr[i]<=n and arr[i]!=arr[correct_pos]:
                arr[i],arr[correct_pos]=arr[correct_pos],arr[i]
                correct_pos=arr[i]-1
                
        for i in range(n):
            if arr[i]!=i+1:
                return i+1
        return n+1
