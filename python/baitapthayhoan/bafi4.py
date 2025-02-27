with open ('bt.inp','r') as f1:
    N=int(f1.readline().strip())
s=''
i=1
while len(s) < N:
    s=s+ str(i**2)
    i += 1
kq=s[N-1]
with open('bt.out','w') as f2:
    f2.write(str(kq))
print(s)