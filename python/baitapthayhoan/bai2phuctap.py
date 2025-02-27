f1= open('bt.inp','r')
f2=open('bt.out','w')
A=f1.readline().split()
k=int(A[0])
B=[]
d=k
for i in range(int(A[1])):
    d =str(d)[::-1]
    d=int(d)
    
    B.append(d)
    d += k
print(B)
    

