import math
f1= open('bt.inp','r')
f2=open('bt.out','w')
def lasonguyento(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def kiemtra(n):
    B=[]
    for i in range(n):
        if i %4==1 and lasonguyento(i):
            B.append(i)
    return B
n=f1.read()
B=kiemtra(int(n))
for i in B:
    f2.write(str(i)+' ')


          


