"""
    Problem 25
    1000-digit Fibonacci number

The decimal library is being used because without it the code
reaches multiple Overflow errors.
"""

from utility.decorators import timeit, printit
from utility.constants import golden
import decimal

golden = decimal.Decimal(golden)


@printit
@timeit
def run():
    i = 2
    c = decimal.Decimal(1)

    while len(str(c)) < 1000:
        c = round(c*golden)
        i += 1

    print(c, i)


if __name__ == "__main__":
    run()
