# Problem 10
# Summation of primes

from utility.decorators import timeit, printit
from utility.math_f import sieve_of_eratosthenes

@printit
@timeit
def run(b):
    primes = sieve_of_eratosthenes(b)
    return sum(primes)

if __name__=="__main__":
    b = 2000000
    run(b)
