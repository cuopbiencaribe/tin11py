with open('test1.inp', 'r') as f1, open('test2.out', 'w') as f2:
    ds=[]
    sum = 0
    n = f1.read().split(',')
    list = map(int, n)
    for i in list:
        if i % 2 == 0:
            sum += 1
            ds.append(i)
    f2.write(str(sum)+"\n" )
    f2.write(' '.join(map(str, ds)))
