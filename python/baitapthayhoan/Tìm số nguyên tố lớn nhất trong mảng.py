# Tìm số nguyên tố lớn nhất trong mảng

def lasonguyento(i):
        if i<2:
            return False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True

def max_snt(ds):
    max=None
    for i in ds:
          if lasonguyento(i) and (max is None or i > max):
               max=i
    return max

def taods():
    n = int(input('Nhập vào số phần tử của danh sách: '))  
    ds = []  
    for i in range(n):  
        ds.append(int(input('Nhập vào phần tử thứ ' + str(i + 1) + ': ')))  
    return ds

if __name__=='__main__':
    ds=taods()
    print('Số nguyên tố lớn nhất trong mảng là:',max_snt(ds))
