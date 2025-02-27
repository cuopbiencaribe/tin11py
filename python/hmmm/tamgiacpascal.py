import time
a=time.time()
def tamgiacpascal(n):
    A=[]
    if n ==1:
        A=[[1]]
    if n >1:
        A=[[1],[1,1]]
        for i in range(2,n):
            B=[1]
            for j in range(1,i):
                B.append(A[i-1][j-1]+A[i-1][j])
            B.append(1)
            A.append(B)
    return A
print(tamgiacpascal(30))
b=time.time()
print('thời gian chạy code là',b-a)            
                
