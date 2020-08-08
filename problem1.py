# Problem 1
# Multiples of 3 and 5

from utility.decorators import timeit

@timeit
def run(mul_of, lt):
    facs = []

    for i in range(1,lt):
        if True in map(lambda a: i%a==0, mul_of):
            facs.append(i)
    
    print(sum(facs))


if __name__=="__main__":
    multiples_of = [3,5]
    less_than = 1000
    run(multiples_of, less_than)
