def run():
    mul_of = [3,5]
    lt = 1000

    facs = []

    for i in range(1,lt):
        if True in map(lambda a: i%a==0, mul_of):
            facs.append(i)
    
    print(sum(facs))


if __name__=="__main__":
    run()
