import threading



# Nhân 2 ma trận vuông 2x2
def multiply_matrix(matrix_1, matrix_2):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return result

# Lũy thừa ma trận
def pow_matrix(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]] # Ma trận đơn vị
    elif n == 1:
        return matrix
    else:
        temp = pow_matrix(matrix, n // 2)
        if n % 2 == 0:
            return multiply_matrix(temp, temp) # mũ chẫn
        else:
            return multiply_matrix(multiply_matrix(temp, temp), matrix) # mũ lẻ

def fibonacci(result, index):
    F = [[1, 1], [1, 0]]
    result[index] = pow_matrix(F, index)[0][1] # Fn=([Fn+1 Fn] [Fn Fn−1]) = ([1 1] [1 0])^n

def fibonacci_parallel(n):
    result = [0] * (n + 1)
    result[0] = 0
    result[1] = 1
    max_threads = 4 
    for i in range(2, n + 1):
        threads = []
        thread = threading.Thread(target=fibonacci, args=(result, i))
        threads.append(thread)
        thread.start()
        if len(threads) == max_threads:
            for thread in threads:
                thread.join()
            threads.clear()
    return result[n]

import time
if __name__ == "__main__":
    start = time.time()
    print(fibonacci_parallel(10))
    end = time.time()
    exetime = end - start
    print("Matrix exetime: ", exetime)

    