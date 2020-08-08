# Problem 3
# Largest prime factor

from utility.decorators import timeit, printit
from utility import math_f

@printit
@timeit
def run(n):
    m = n
    i = 2
    while i*i<m:
        while m%i==0:
            m/=i
        i += 1
    return m

if __name__=="__main__":
    number = [13195, 600851475143, 20]
    run(number[1])
