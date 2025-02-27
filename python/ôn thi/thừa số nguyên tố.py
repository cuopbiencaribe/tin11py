def primes_factors(n):  
    factors = []   
    while n % 2 == 0:  
        factors.append(2)  
        n //= 2  
    for i in range(3, int(n**0.5) + 1):  
        while n % i == 0:  
            factors.append(i)  
            n //= i  
    if n > 1:  
        factors.append(n)  
    return factors  

 
with open('test1.txt', 'r') as f:  
    numbers = [int(line.strip()) for line in f]  
 
with open('test2.txt', 'w') as f:  
    for number in numbers:  
        factors = primes_factors(number)  
        f.write(" ".join(map(str, factors)) + '\n')