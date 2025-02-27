l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = ''.join(map(str, l1[::-1]))
l1 = int(l1)
l2 = ''.join(map(str, l2[::-1]))
l2 = int(l2)

result = l1 + l2

print("Kết quả của phép cộng là:", result)
