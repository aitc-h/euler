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
