    def calculateSpan(self,price,n):
        stack=[]
        res=[]
        for i in range(n):
            if len(stack)==0:
                res.append(-1)
            elif len(stack)>0 and stack[-1][0]>a[i]:
                res.append(stack[-1][1])
            elif len(stack)>0 and stack[-1][0]<=a[i]:
                while (len(stack)>0 and stack[-1][0]<=a[i]):
                    stack.pop(-1)
                if len(stack)==0:
                    res.append(-1)
                else:
                    res.append(stack[-1][1])
            stack.append([a[i],i])
            
        for i in range(len(res)):
            res[i]=i-res[i]
        return res
