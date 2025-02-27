ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s=0
for i in ma_tran:
    for j in i:
        s+=j
print(s)