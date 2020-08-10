"""
    Problem 15
    Lattice Paths

My first attempt at this problem involved iterating over all possible binary numbers between 0 and 2^(2n),
which as you can probably guess got big fast. I dread to think of the time complexity.

Then I took a mathematical look at the sequence trying to find some sort of pattern, and when I couldn't
see one, did what any good programmer does in times of need: Googled it.
Putting the first few terms of the sequence into Google gives the oeis.org page for
"Central binomial coefficients" (A000984). This gives the formula for finding the nth term:
    binomial(2*n,n) = (2*n)!/(n!)^2
which gives the correct answer in a more reasonable amount of time.
"""

from utility.decorators import timeit, printit
from utility.math_f import factorial


@printit
@timeit
def run(n):
    x = factorial(2*n)
    y = factorial(n)
    return int(x/(y**2))


if __name__ == "__main__":
    n = 20
    k = run(n)
