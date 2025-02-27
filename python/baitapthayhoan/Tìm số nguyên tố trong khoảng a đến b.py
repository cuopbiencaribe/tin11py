# Tìm n số nguyên tố đầu tiên
def lasonguyento(i):
        if i<2:
            return False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True
a=int(input('Nhập a: '))
b=int(input('Nhập b: '))
print(f'Số nguyên tố trong khoảng từ {a} đến {b} là:',end=' ')
for i in range(a,b+1):
     if lasonguyento(i):
          print(i,end=' ')