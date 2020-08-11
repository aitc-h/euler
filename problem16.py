"""
    Problem 16
    Power digit sum

I think this is meant to be more difficult in languages
which have difficulties handling larger numbers.
"""

from utility.decorators import timeit, printit


@printit
@timeit
def run():
    print(sum(list(map(int, str(2**1000)))))


if __name__ == "__main__":
    run()
