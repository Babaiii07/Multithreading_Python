from multiprocessing import Pool

def f(array) :
    return array*array

if __name__ == "__main__" :
    array = [2,3,5]
    p = Pool()
    result = p.map(f,array)
    print(result)



