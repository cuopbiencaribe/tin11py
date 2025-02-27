# bài tập chuỗi tiền lùi giống nhau
s = "A man, a plan, a canal: Panama"

def kiemtra (s):
    s=s.lower()
    ds=''
    for i in s:
        if i.isalnum():
            ds=ds+i
    return ds==ds[::-1]
    
print(kiemtra(s))  # Output: True
print(kiemtra("race a car"))  # Output: False
print(kiemtra(" "))  # Output: True

