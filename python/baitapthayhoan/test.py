f1=open('bt.inp','r')
f2=open('bt.out','w')
a=f1.readline().strip()
b=f1.readline().strip()
def timkiemsau(a,b):
    d=[]
    index=0
    while True:
        c=b.find(a,index)
        if c == -1:
            break
        d.append(c)
        index = c+1
    if len(d)!=0:
        return d
    else:
        return -1
a=timkiemsau(a,b)
f2.write(str(a))
