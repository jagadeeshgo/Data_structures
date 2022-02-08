  #time complexity is slightly greater than O(n)
  #1st approach
  def findTwoElement( self,arr, n): 
        # code here
        i=0
        
        while i<n:
            if arr[i]!=arr[arr[i]-1]:
                arr[i],arr[arr[i]-1]=arr[arr[i]-1],arr[i]
            else:
                i+=1
        #return arr
                
        for i in range(n):
            if arr[i]!=i+1:
                return arr[i],i+1
              
              
    # 2nd approach
              
    def findTwoElement( self,arr, n):
        
        # code here
        set_of_arr=set(arr)
        #duplicate element
        n1=sum(arr)-sum(set_of_arr)
        #missing element
        n2=abs(sum(set_of_arr)-n*(n+1)//2)
        
        return n1,n2
