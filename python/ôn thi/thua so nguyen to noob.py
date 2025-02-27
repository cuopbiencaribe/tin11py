def thuasonguyento(n):
    factors=[]
    i=2
    while n!=1:
        while n%i==0:
            factors.append(i)
            n //=i
        i +=1
    return factors
n=int(input('Nhap so nguyen duong n: '))
print('Thua so nguyen to cua',n,'la: ',thuasonguyento(n))