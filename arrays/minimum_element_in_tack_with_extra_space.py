# minimum element in stack with extra space
arr=[18,19,29,15]
stack=[]
support_stack=[]

def push(a):
    stack.push(a)
    if len(support_stack)==0 or a<=support_stack[-1]:
        support_stack.push(a)
    return a

def pop(a):
    if len(support_stack)==0:
        return -1
    ans=stack[-1]
    stack.pop(a)
    if ans==support_stack[-1]:
        support_stack.pop(a)
    return ans

def get_min(a):
    if len(support_stack)==0:
        return -1
    return support_stack[-1]
