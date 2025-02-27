
def sapxep (lst):
    n=len(lst)
    for i in range (n):
        for j in range (n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
A=[9,6,7,5,3,4,2,1,8]
print(sapxep(A))