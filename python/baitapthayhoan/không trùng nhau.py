A=[1,1,2,3,4,2,4,2,3,2,4,1,5,2,5,2,5,2,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
dulieu=[]
for i in A:
    if i not in dulieu:  # Thêm lần lượt i vào B nếu i không nằm trong N . Còn nếu i đã nằm trong B thì không thêm vào nữa
        dulieu.append(i)
print(dulieu)