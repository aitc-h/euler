# Problem 14
# Longest Collatz sequence

from utility.decorators import timeit, printit


def collatz(n):
    if n & 1 == 0:
        return int(n/2)
    else:
        return (3*n) + 1


def chain(n):
    count = 1
    while n != 1:
        n = collatz(n)
        count += 1
    return count


@printit
@timeit
def run():
    longest = 0
    longest_i = 0
    for i in range(1, 1000000):
        c = chain(i)
        if c > longest:
            longest = c
            longest_i = i
    print(longest_i)


if __name__ == "__main__":
    run()
