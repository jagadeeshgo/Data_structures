# minimum element in stack with O(1) complexity

min_ele=0

def get_min_elemet():
    if len(stack)==0:
        return -1
    return min_ele

def push(x):
    if len(stack)==0:
        return -1
    elif x>=min_ele:
        stack[-1]=x
    elif x<min_ele:
        stack[-1]=2*x-min_ele
    
def pop():
    if len(stack)==0:
        return -1
    elif stack[-1]=>min_ele:
        stack.pop(-1)
    elif stack[-1]<min_ele:
        min_ele=2*min_ele-stack[-1]
        stack.pop(-1)

def top():
    if len(stack)==0:
        return -1
    elif stack[-1]<min_ele:
        return min_ele
    elif stack[-1]>min_ele:
        return stack[-1]
