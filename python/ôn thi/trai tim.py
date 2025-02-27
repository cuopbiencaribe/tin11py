def nenso(n):
    dem=0
    while n!=2:
        for i in range(2,n):
            if n%i!=0:
                n=i
                dem+=1
                break
    return dem
tong=0
for i in range(4,6+1):
    tong+=nenso(i)
    print(f'độ nén của {i} là',nenso(i))
print('tổng độ nén là',tong)
