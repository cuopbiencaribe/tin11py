import randommm
A=[]
for i in range(100):
    A.append(random.randint(1,100))
def timcapso(A,k):
    day=[]
    n=len(A)
    for a in A:
        b=k-a
        if b in A:
            day.append([a,b])

    return day
print((timcapso(A,100)))
