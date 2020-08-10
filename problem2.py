"""
    Problem 2
    Even Fibonacci Numbers
"""

from utility.decorators import timeit
from utility.constants import golden


def next_fib(i):
    return round(i*golden)


@timeit
def run(lt):
    terms = []
    i = 1
    while i < lt:
        if i % 2 == 0:
            terms.append(i)
        i = next_fib(i)
    return sum(terms)


if __name__ == "__main__":
    less_than = 4_000_000

    print(run(less_than))
