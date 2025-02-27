mk=input('Nhập vào mật khẩu: ')
def ktr(mk):
    
    x=0
    y=0
    for i in mk:
        if i.isalpha():
            x +=1
        if i.isdigit():
            y +=1
    return x,y
i=1
while i <5:
    x,y=ktr(mk)
    if len(mk)<6:
        mk=input('Nhập lại mật khẩu: ')
    elif x ==0:
        mk=input('Vui lòng nhập mật khẩu có ít nhất 1 chữ: ' )
    elif y==0:
        mk=input('Vui lòng nhập mật khẩu có ít nhất 1 số: ')
    elif mk.isalnum() == True:
        mk=input('Vui lòng nhập mật khẩu có ít nhất 1 ký tự đặc biệt: ')
    else:
        break
    i +=1

print('Bạn đã nhập quá 5 lần sai. Chương trình kết thúc.')

print('Mật khẩu được nhập đã đúng')

      
