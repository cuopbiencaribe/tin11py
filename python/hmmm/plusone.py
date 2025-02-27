# plus one
A=[1,2,3]
def plusOne(A):
    A=''.join(map(str,A))
    A=int(A)
    A+=1000
    return A
print(plusOne(A))