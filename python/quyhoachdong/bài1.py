f1=open('baitap.inp','r')
f2=open('bt.out','w')
def fibo(n):
    if n ==1:
        return 1
    if n ==2:
        return 1
    return fibo(n-1)+ fibo(n-2)
A=[]
for dong in f1:
    s=dong.strip()
    A.append(s)
for i in range(1,len(A)):
    f2.write(str(fibo(int(A[i])))+'\n')
f1.close()
f2.close()