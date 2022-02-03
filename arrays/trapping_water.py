    
  
    def trappingWater(self, arr,n):
        
        max_left=[0]*n
        max_right=[0]*n
        max_left[0]=arr[0]
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],arr[i])
            
        max_right[n-1]=arr[n-1]
        for j in range(n-2,-1,-1):
            max_right[j]=max(max_right[j+1],arr[j])
        
        min_arr=[0]*n
        for i in range(n):
            min_arr[i]=min(max_left[i],max_right[i])
        #return max_right
        water=[0]*n
        for i in range(n):
            water[i]=min_arr[i]-arr[i]
        
        return sum(water)
