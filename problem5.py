# Problem 5
# Smallest multiple

from utility.decorators import timeit, printit
from utility import math_f

def convert(l):
    out = {}
    for i in l:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    return out

def redu(d):
    total = 1
    for i in d:
        total *= (i**d[i])
    return total

@printit
@timeit
def run(n):
    primes = math_f.sieve_of_eratosthenes(n)
    freq = {i:0 for i in primes}
    for i in range(2,n):
        x = math_f.get_prime_divisors(i)
        y = convert(x)
        for key in y:
            if freq[key] < y[key]:
                freq[key] = y[key]
    ans = redu(freq)
    return ans

if __name__=="__main__":
    n = 20
    run(n)
