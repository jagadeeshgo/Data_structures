	def rowWithMax1s(self,arr, n, m):
		# code here
		#approach 1 worst time complexity O(n*m)
		'''
		for col in range(0,m):
		    for row in range(0,n):
		        if arr[row][col]==1:
		            return row
	    return -1
	    '''
	    #approach 2 tc O(n+m)
	    
	    j=m-1
	    r=0
	    while j>=0 and arr[0][j]==1:
	        j-=1
	    
	    for i in range(1,n):
	        while(j>=0 and arr[i][j]==1):
	            j-=1
	            r=i
	    if j==m-1:
	        return -1
	    else:
	        return r
