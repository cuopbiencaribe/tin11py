A = [28,6,22,8,44,17]
B = [22,28,8,6]
C=[]
for i in B:
    C.extend([j for j in A if j ==i])
C.extend(sorted([x for x in A if x not in B]))
print(C)

