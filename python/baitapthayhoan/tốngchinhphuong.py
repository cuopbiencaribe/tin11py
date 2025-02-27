
def lasonguyento(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def lasochinhphuong(x):
    if int((x**(0.5)))**2 ==x:
           return True
    return False
def kiemtra(n):
    b = 0
    if lasonguyento(n)==False:
       return 'không là nguyên tố'
    for a in range(n):
        b=n-a
        if lasochinhphuong(a) and lasochinhphuong(b):
            return a,b
n=int(input('Nhập vào s'))

print(kiemtra(n))