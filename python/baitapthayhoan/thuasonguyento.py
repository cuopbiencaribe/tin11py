def thuasonguyento(n):
    A=[]
    i = 2
    while n !=1:
        while n % i == 0:
            A.append(i)
            n //= i
        i += 1
    return A
n=int(input('Nhập vào số n: '))
print(thuasonguyento(n))