f1= open('bt.inp','r')
f2=open('bt.out','w')
n=f1.read()
b=0
a=0
A=[]
for i in range(1,int(n)//2):
    b=int(n)-i
    if b != i:
        A.append([i,b])
        a += 1
for i in range(len(A)):
        f2.write(str(A[i][0])+' '+str(A[i][1]))
        if i  < len(A)-1:
            f2.write(',')
f2.write('\n'+ str(a) )


    