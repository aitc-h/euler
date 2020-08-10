# Problem 12
# Highly divisible triangular number

from utility.decorators import timeit, printit
from utility.math_f import sum_naturals_to_n, get_divisors
from math import ceil, sqrt


def div_count(n):
    # Returns the count of divisors of a number
    total = 0
    for i in range(1, int(ceil(sqrt(n)))+1):  # Check up to sqrt(n)
        if n % i == 0:  # If i is a factor then n/i is also a factor
            total += 2
        if i*i == n:  # If i is the sqrt(n) then it is a square (only one factor)
            total -= 1
    return total


@printit
@timeit
def run(m):
    for n in range(1, 1000000):
        if n % 2 == 0:
            cnt = div_count(n/2) * div_count(n+1)
        else:
            cnt = div_count(n) * div_count((n+1)/2)

        if cnt >= m:
            return sum_naturals_to_n(n)


if __name__ == "__main__":
    n = 500
    run(n)
