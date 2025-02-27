def daydainhat(ds):
    n=len(ds)
    day=[]
    daymax=[]
    sl=1 #lúc dầu đã chọn i-1 là phần tử đầu tiền rồi
    for i in range(1,n):
        if ds[i] ==ds[i-1]+1: # nếu phần tử phía sau lớn hơn phía trước 1 đơn vị
            if sl==1: # dùng cái này để chỉ thêm 2 phần tử vào ds 1 lần duy nhất thôi
                day.append(ds[i-1])
            day.append(ds[i])
            sl+=1
        else:
            if len(day)>len(daymax): # nếu ds tạm thời lớn hơn danh sách chính
                daymax=day
            day=[]
            sl=1
    return daymax
day=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,15,11]
print(daydainhat(day))