import time
import threading
def calculate_square(list) :
    print("calculating square of a list:-")
    for i in list :
        time.sleep(0.2)
        print(f"square :- {i*i}\n")
    

def calculate_cube(list) :
    print("calculating cube of list")
    for i in list:
        time.sleep(0.2)
        print(f" cube :- {i*i*i}\n")

list = [2,3,8,9]
t1 = threading.Thread(target=calculate_cube,args=(list,))
t1.start()
t2 = threading.Thread(target=calculate_square,args=(list,))
t2.start()
t1.join()
t2.join()
t = time.time()
print(f"done :- {time.time() - t}")