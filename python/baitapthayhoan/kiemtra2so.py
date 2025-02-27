import math
f1= open('bt.inp','r')
f2=open('bt.out','w')
A=[]
for i in range(2):
    s=f1.readline().strip()
    A.append(s)
k='0'*abs(len(A[1])-len(A[0]))
if len(A[1]) > len(A[0]):
    A[0]= k +A[0]
if len(A[1]) < len(A[0]):
    A[1]= k+ A[1]
if A[0]> A[1]:
    f2.write('1')
if A[0] < A[1]:
    f2.write('-1')
if A[0]== A[1]:
    f2.write('0')