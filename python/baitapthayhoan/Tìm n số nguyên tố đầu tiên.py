# Tìm n số nguyên tố đầu tiên
def lasonguyento(i):
        if i<2:
            return False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                return False
        return True

def main(n):
    snt=[]
    num = 2
    while len(snt)<n:
        if lasonguyento(num):
               snt.append(num)
        num+=1
    return ' '.join(map(str,snt))

if __name__=='__main__':
    n=int(input('Nhập số lượng nguyên tố cần tìm:'))
    print((main(n)))

    
          