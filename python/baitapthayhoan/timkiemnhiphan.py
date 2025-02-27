# Tìm kiếm nhị phân
def timkiemnhiphan(arr,k):
    dau=0
    cuoi=len(arr)
    giua=0
    while dau<cuoi:
        giua=(dau+cuoi)//2
        if k == arr[giua]:
            return giua
        if k > arr[giua]:
            dau= giua+1
        if k < arr[giua]:
            cuoi= giua-1
    return -1

print(timkiemnhiphan([1,2,3,4,5,6,7,8],5))
