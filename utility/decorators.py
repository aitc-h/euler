import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed

def printit(method):

    def printer(*args, **kw):
        result = method(*args, **kw)
        print(result)
        return result
    
    return printer
