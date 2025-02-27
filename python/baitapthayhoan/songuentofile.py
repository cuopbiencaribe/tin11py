f1=open('bt.inp','r')
f2=open('bt.out','w')
day=list(map(int,f1.read().strip().split()))

def lasonguyento(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def check(day):
    for i in day:
        if lasonguyento(i):
            f2.write(str(i)+' ')
    return
check(day)


