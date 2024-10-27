import multiprocessing

def calculate_square(n, result,v):
    print("inside the process it will change the value of v.value")
    v.value = 0.0
    for idx, i in enumerate(n):
        result[idx] = i * i

if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array("i", len(numbers))  
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calculate_square, args=(numbers, result,v))

    p.start()
    p.join()

    # print(result[:])
    print(v.value)