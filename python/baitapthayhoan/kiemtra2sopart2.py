import math
f1= open('bt.inp','r')
f2=open('bt.out','w')
A=[]
for i in range(2):
    s=f1.readline().strip() 
    
    A.append(s)
    A=list(map(int,A))
if A[0]> A[1]:
    f2.write('1')
if A[0] < A[1]:
    f2.write('-1')
if A[0]== A[1]:
    f2.write('0')
print(math.log(A[0],10))