ds=[1,2,3,4,5,6]
chan=[]
le=[]
for i in ds:
    if i%2==0:
       chan.append(i)
    else:
        le.append(i)
print('các số chẵn là', *(k for k in chan),end='')
print('\ncác số lẽ là',*(j for j in le),end=' ')