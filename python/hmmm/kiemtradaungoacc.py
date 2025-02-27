def isValid(ds):
    stack=[]
    pairs = {')': '(', ']': '[', '}': '{'}
    for i in ds:
        if i in '({[':
            stack.append(i)
        else:
            if not stack or stack[-1]!= pairs[i]:
                return False
            stack.pop()
    return not stack
ds="{[(])}" 
print(isValid(ds))
