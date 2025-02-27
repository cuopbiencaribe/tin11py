A=[10,22,9,41,50]
d=[1]*len(A)
for i in range(1,len(A)):
    for j in range(i):
        if A[i] > A[j]:
            d[i]=max(d[j]+1,d[i])
print(max(d))

