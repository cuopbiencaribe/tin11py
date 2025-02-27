import time
import random
f1=open('bt.out','w')
A = []
start=time.time()
for i in range(1000000):
    A.append(random.randint(1,100))
n=len(A)
max=0
k=A[0]
B=[]
for i in range(0,n-2):
        k = A[i] + A[i+1] + A[i+2]
        if k > max:
            max=k
            B.clear()
            B.append([A[i],A[i+1],A[i+2]])
print(B,max)
f1.write(str(B)+str(max))
end=time.time()
print(end-start)







