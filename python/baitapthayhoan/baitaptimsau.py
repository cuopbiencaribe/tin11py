f1=open('bt.inp','r')
f2=open('bt.out','w')
a=f1.readline().strip()
b=f1.readline().strip()
c=0
A=[]
for i in range(len(b)):
    if b[i] == a[0] and b[i+1:i+len(a)] == a[1:]:
        A.append(i)

print(c)
        
print(A)
