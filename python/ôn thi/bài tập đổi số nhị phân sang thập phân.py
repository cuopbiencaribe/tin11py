def chuyendoi(A):
    C=0
    B=(A[::-1])
    for i in range (len(B)):
        num=int(B[i])
        C=C+num*2**(i)
    return C

with open ('test1.txt','r') as in_p , open ('test2.txt','w') as ou_t:
    for line in in_p:
        C=chuyendoi(line)
        ou_t.write(str(C))

