# tính tổng từ 1 đến n bằng đệ quy
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(5))