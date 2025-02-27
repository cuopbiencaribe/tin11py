# hàm tìm ước chung lớn nhất của 2 số
def uocchungcong(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def uocchungchia(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
print("Ước chung lớn nhất của 2 số là: ",uocchungcong(a,b))
print("Ước chung lớn nhất của 2 số là: ",uocchungchia(a,b))
    