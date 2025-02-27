def pfnum(n):
    s=0
    for i in range(1,n//2+1):
        if n %i ==0:
            s=s+i
    return s==n
start = int(input("......"))
end = int(input("......"))

print(f"Perfect numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if pfnum(i):
        print(i)



