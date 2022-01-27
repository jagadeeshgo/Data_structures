class Solution:
	def minJumps(self, arr, n):
	    #code here
	    goal = len(arr) -1
	    count=0
	    for i in range(len(arr)-1,-1,-1):
	        if i+arr[i]>=goal:
	            goal=i
	            count+=1
	            
	    return count if goal==0 else -1
    
    #time complexity O(n)
    
    #to check if we can reach the goal in the given array (i.e end of array)
