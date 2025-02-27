A=[3,6,1,0]
def gapdoi(A):
    a=max(A)
    A.remove(a)
    b=max(A)
    if a/b >=2:
        return 1
    return -1
print(gapdoi(A))
