import sys
import time
import math


def isPrime(n):
    loops = 0
    for i in range(2,n):
        loops += 1
        if i > math.sqrt(n): 
            break 
        else: 
            if n % i == 0:
                return False
    #print(loops)
    return True

def slowIsPrime(n):
    loops = 0
    for i in range(2,n):
        loops += 1
        if n % i != 0: 
            continue
        else: 
            return False
    print(loops)
    return True


def pirmesInRange(start,stop):
    print("Primes in range from " + str(start) + " to " + str(stop) + " are: ")
    for i in range(start, stop):
        if isPrime(i):
            print(i)

def factorize(n): 
    if isPrime(n): 
        return " Primie number can not be factorized! "
    else:
        primes = {}
        x = 0
        for i in range(2,n): 
            if isPrime(i):
                primes[x] = i
                x += 1      
        y = 0
        factors = []
        while n > 1 : 
            if n % primes[y] == 0:
                factors.append(primes[y])
                n = n / primes[y]
            else:
                y += 1
    return factors 

def slow_factorize(n): 
    if isPrime(n): 
        return " Primie number can not be factorized! "
    else:
        primes = {}
        x = 0
        for i in range(2,n): 
            if slowIsPrime(i):
                primes[x] = i
                x += 1      
        y = 0
        factors = []
        while n > 1 : 
            if n % primes[y] == 0:
                factors.append(primes[y])
                n = n / primes[y]
            else:
                y += 1
    return factors 

#------------------------------------------------------------------------------------

def main():
    t1 = time.time()
    print(factorize(187))
    # pirmesInRange(0,100)    
    t2 = time.time()
    print(t2 - t1) 

    # print(isPrime(100001))
    
if __name__ == "__main__":
    main()