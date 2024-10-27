

def fact(n) :
    return n*n


if __name__ == "__main__" :
    array = [2,3,5]
    t = []
    for i in array:
        t.append(fact(i))
    print(t)