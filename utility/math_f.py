import math

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    
    return True

def is_even(n):
    return n&1 == 0

def get_divisors(n):
    for i in range(1, int(n/2)+1):
        if n%i==0:
            yield i
    yield n

def get_divisors_reversed(n):
    for i in range(int(n/2)+1, 1, -1):
        if n%1==0:
            yield i
    yield n

def get_prime_divisors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            factors.append(int(i))
            n = math.floor(n / i)
    if n > 2:
        factors.append(int(n))
    return factors


def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False

    nums = list(filter(lambda i: prime[i], range(n+1)))
    return nums
