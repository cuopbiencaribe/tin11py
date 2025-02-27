A=[1,2,3,4,5,6,7,8]
def timkim(A,k):
    end= len(A)
    start=0
    while end > start:
        mid= (end + start)//2
        if A[mid]==  k:
            return mid
        if A[mid] > k:
            start = mid +1
        if A[mid] < k:
            end = mid -1
    return -1
print(timkim(A,5))