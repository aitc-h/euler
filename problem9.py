"""
    Problem 9
    Special Pythagorean triplet
"""

from utility.decorators import timeit, printit


def is_pythag(a, b, c):
    return a**2 + b**2 == c**2


def is_answer(a, b, c):
    return a+b+c == 1000


@printit
@timeit
def run():
    a, b, c = 1, 1, 1
    s = 1000
    found = False
    for a in range(1, int(s/3)):
        for b in range(a, int(s/2)):
            c = s-a-b
            if is_pythag(a, b, c):
                found = True
                break
        if found:
            break
    return a, b, c


if __name__ == "__main__":
    answer = run()
    print(answer[0] * answer[1] * answer[2])
