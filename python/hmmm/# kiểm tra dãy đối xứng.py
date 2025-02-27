# kiểm tra dãy đối xứng
def tinhdoixung(A):
    n=len(A)
    for i in range(n //2):
        if A[i] != A[n-i-1]: # khi i càng tăng thì n-i-1 càng giảm
            return False
        return True
A=[1,2,3,4,5,4,3,2,1]
if tinhdoixung(A): 
    print('Dãy đối xứng')
else:
    print('Dãy không đối xứng')

