import multiprocessing
import time


#this is the problem of multiprocessing lock


def deposite(balance) :
    for i in range(100) :
        time.sleep(0.01)
        balance.value = balance.value + 1

def withdraw(balance) :
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1


if __name__ == "__main__" :
    balance = multiprocessing.Value('i', 200)
    p = multiprocessing.Process(target=deposite , args = (balance,))
    d = multiprocessing.Process(target=withdraw , args = (balance,))

    p.start()
    d.start()
    p.join()
    d.join()
    i = 0
    print(balance.value)