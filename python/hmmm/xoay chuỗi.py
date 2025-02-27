# xoay chuỗi
nums = [-1,-100,3,99]
k=2
A=nums[len(nums)-k:]
A.extend(nums[:len(nums)-k])
print(A)