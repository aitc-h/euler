"""
    Problem 6
    Sum square difference
"""

from utility.decorators import timeit, printit


@printit
@timeit
def run(n):
    x = n + 1
    a = (3*n*x)-(2*(2*n+1))
    b = a*n*x*(1/12)
    return int(b)


if __name__ == "__main__":
    n = 100
    run(n)
