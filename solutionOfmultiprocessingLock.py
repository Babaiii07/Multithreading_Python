#in this solution i am using multiprocessing lock


import multiprocessing
import time


def deposite(balance,l) :
    for i in range(100) :
        time.sleep(0.01)
        l.acquire()                                   #critical section
        balance.value = balance.value + 1             #critical section
        l.release()                                  #critical section

def withdraw(balance,l) :
    for i in range(100):
        time.sleep(0.01)
        l.acquire()                                  #critical section
        balance.value = balance.value - 1            #critical section
        l.release()                                  #critical section


if __name__ == "__main__" :
    balance = multiprocessing.Value('i', 200)
    l = multiprocessing.Lock()
    p = multiprocessing.Process(target=deposite , args = (balance,l))
    d = multiprocessing.Process(target=withdraw , args = (balance,l))

    p.start()
    d.start()
    p.join()
    d.join()
    i = 0
    while i <= 10:
        print(balance.value)
        i = i + 1