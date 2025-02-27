# chuyển từ nhị phân sang thập phân
A='1111'
C=0
A=(A[::-1])
for i in range (len(A)):
    
    C=C+(int(A[i]))*2**(i)
print(C)
'''Giải thích:
Để đổi số nhị phân sang số thập phân ta đánh số thứ tự cho từng 
số từ phải sang trái(tính từ 0 đến len của dãy) rồi lấy số đó nhân cho
2 mũ chỉ số
Trong bài này ta sẽ đảo ngược chuỗi lại để đánh dấu cho các số từ phải 
sang trái chỉ số từ 0 đến len của dãy
rồi lấy số đó nhân cho 2 mũ chỉ số

'''