from multiprocessing import Pool
import time


def f(n) :
    sum = 0
    for i in range(100):
        sum += i*i
    return sum
    
if __name__ == "__main__" :
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(100000))
    p.close()
    p.join()

    print("pool took :- ", time.time() - t1)


    t2 = time.time()
    result = []

    for i in range(100000):
        result.append(f(i))


    print("serial processing took:- ", time.time() - t2)