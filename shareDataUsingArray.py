import multiprocessing

def calculate_square(n, result):
    for idx, i in enumerate(n):
        result[idx] = i * i

if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array("i", len(numbers))  
    p = multiprocessing.Process(target=calculate_square, args=(numbers, result))

    p.start()
    p.join()

    print(result[:])
