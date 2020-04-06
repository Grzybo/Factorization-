import sys
import time
import math


def isPrime(n):
    for i in range(2,n):
        if i > math.sqrt(n): 
            break 
        else: 
            if n % i == 0:
                return False
    return True


def PirmesInRange(start,stop):
    print("Primes in range from " + str(start) + " to " + str(stop) + " are: ")
    for i in range(start, stop):
        if isPrime(i):
            print(i)

def Factorize(n): 
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

#------------------------------------------------------------------------------------

def main():
    t1 = time.time()
    print(Factorize(111001))    
    t2 = time.time()
    print(t2 - t1)

if __name__ == "__main__":
    main()