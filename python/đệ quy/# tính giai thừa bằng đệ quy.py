# tính giai thừa bằng đệ quy
def giaithua(n):
    if n==1:
        return 1
    return n*giaithua(n-1)
print(giaithua(700))