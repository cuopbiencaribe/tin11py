import random
A=[]
for i in range(100):
    A.append(random.randint(1,100))
def maxmin(A):
    max=A[0]
    min=A[0]
    for i in A:
        if i > max:
            max=i
        elif i < min:
            min=i
    return max,min
max,min=maxmin(A)
print(f'Số lớn nhất là {max} \nSố nhỏ nhất là {min}')
