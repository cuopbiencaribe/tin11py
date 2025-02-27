# hàm để tạo danh sách tất cả các số đề cho
def dayso(A):
    for i in range(3,1001):
        k=A[i-1]+A[i-3]
        A.append(k)
    return A

A=[1,1,1]
A=dayso(A)
with open ('test1.txt','r') as in_p , open ('test2.txt','w') as ou_t:
    h=in_p.readline()
    ou_t.write(str(A[int(h)-1]))
        