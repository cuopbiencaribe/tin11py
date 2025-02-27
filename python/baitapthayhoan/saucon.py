f1= open('bt.inp','r')
f2=open('bt.out','w')
s=f1.read().strip()
A=[]
ds=''
for i in s:
    A.append(i)
    for j in range(1,len(s)):
        if i != s[j] :
            i=i+s[j]
            if i[::-1] not in A:
                A.append(i)
print(A)