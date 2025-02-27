def lasonguyento(i):
        if i<2:
            return False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True

def min_snt(ds):
    min=None
    for i in ds:
        if lasonguyento(i) and (min is None or i <min):
            min=i
    return min

def taods():
    n = int(input('Nhập vào số phần tử của danh sách: '))  
    ds = []  
    for i in range(n):  
        ds.append(int(input('Nhập vào phần tử thứ ' + str(i + 1) + ': ')))  
    return ds

if __name__=='__main__':
    ds=taods()
    print('Số nguyên tố nhỏ nhất trong mảng là:', min_snt(ds))