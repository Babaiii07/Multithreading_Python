import multiprocessing

def calculate_square(n, q):
    for idx, i in enumerate(n):
        q.put(i*i)

if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array("i", len(numbers))  
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=calculate_square, args=(numbers, q))

    p.start()
    p.join()

    while q.empty() is False:
        print(q.get())
