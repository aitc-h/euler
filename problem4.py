# Problem 4
# Largest palindrome product

from utility.decorators import timeit, printit

def is_palindrome(n):
    x = str(n)
    y = x[::-1]
    return x==y

@printit
@timeit
def run(n):
    max_pal = 0
    for i in range((10**n)-1, 10**(n-1), -1):
        for j in range((10**n)-1, 10**(n-1), -1):
            k = i*j
            if is_palindrome(k) and k > max_pal:
                max_pal = k
    return max_pal

if __name__=="__main__":
    length = 3
    run(length)
