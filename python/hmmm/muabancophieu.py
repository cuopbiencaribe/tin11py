# highest profit from buy and sell stock
''' Bài này đầu tiên tìm ngày mà giá thấp nhất để mua
rồi tìm ngày giá cổ phiếu cao nhất để bán
Nếu ngày mà giá thấp nhất là ngày cuối cùng thì không có lợi nhuận'''
prices =[1,1,1,1,1,1,1,1,1,1,1]
min=prices[0]
max=0
min_index = 0
for i in range (len(prices)):
    if prices[i] < min:
        min=prices[i]
        min_index=i
if min_index== len(prices)-1:
    print('Không có lợi nhuận')
else:
    for j in range(min_index, len(prices)):
        if prices[j] > max:
            max= prices[j]
    print(f'Lợi nhuận là {max-min}')