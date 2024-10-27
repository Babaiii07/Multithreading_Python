import multiprocessing
import time

def calculate_square(list) :
    print("calculating square of a list:-")
    for i in list :
        time.sleep(2)
        print(f"square :- {i*i}\n")
    

def calculate_cube(list) :
    print("calculating cube of list")
    for i in list:
        time.sleep(2)
        print(f" cube :- {i*i*i}\n")

if __name__ == "__main__" :
    t = time.time()
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calculate_square , args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube , args=(arr,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("huh i am done with my all work")