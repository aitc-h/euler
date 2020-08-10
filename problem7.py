"""
    Problem 7
    10001st Prime
"""

from utility.decorators import timeit, printit
from utility.math_f import sieve_of_eratosthenes


@printit
@timeit
def run():
    x = sieve_of_eratosthenes(104750)
    # x = sieve_of_eratosthenes(15)
    return max(x), x.index(max(x))+1


if __name__ == "__main__":
    run()
