# find pivot index
''' ở bài này ta tạo một danh sách P với các phần tử là tổng các phần tử của danh sách A trước 
nó với P[j]=P[j-1]+A[j]
rồi tiếp tục dựa vào đó để đánh giá các điều kiện '''
A=[1,2,3]
P=[]
s=0
for i in A:
    s=s+i
    P.append(s)
print(P)
pivot_index=-1
for j in range(1,len(A)-1):
    if P[j-1]==P[-1]-P[j]:
        pivot_index=j
print(pivot_index)


