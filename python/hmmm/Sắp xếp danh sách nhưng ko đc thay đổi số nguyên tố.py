# Sắp xếp danh sách nhưng ko đc thay đổi số nguyên tố
def lasonguyento(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def sapxep(A):  
    n = len(A)  
    for i in range(n):  
        min_index = i  # Đổi tên biến để rõ nghĩa hơn  
        for j in range(i + 1, n):  
            if A[j] < A[min_index]:  # So sánh với A[min_index] thay vì A[i]  
                min_index = j  
        # Hoán đổi chỉ khi min_index khác i  
        if min_index != i:  
            if lasonguyento(A[min_index])== False:
                A[i], A[min_index] = A[min_index], A[i]  
    return A  
print(sapxep([1,3,2,4,5,7,9,11]))