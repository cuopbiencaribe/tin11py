# tìm số arstrong trong khoảng cho trước
def armstrong(num):
    n=len(str(num))
    s=0
    for i in str(num):
        s=s+(int(i))**n
    return s==num
start = int(input("......."))
end = int(input("..........."))
found= False
print(f"Armstrong numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if armstrong(i):
        print(i)
        found= True
if not found:
    print(f'Không thì thấy số..')