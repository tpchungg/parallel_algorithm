import threading

def multiply(matrix_a, matrix_b, result, index_A, index_B, size, semaphore):
    with semaphore:  # Đảm bảo chỉ tối đa 4 thread chạy cùng lúc
        temp_sum = 0
        for k in range(size):
            temp_sum += matrix_a[index_A][k] * matrix_b[k][index_B]
        result[index_A][index_B] = temp_sum

def parallel_multiply_matrices(matrix_a, matrix_b):
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    size = len(matrix_a[0])  # Số cột của matrix_a (cũng là số hàng của matrix_b)
    
    semaphore = threading.Semaphore(4)  # Giới hạn số lượng thread tối đa là 4
    threads = []

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            thread = threading.Thread(target=multiply, args=(matrix_a, matrix_b, result, i, j, size, semaphore))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()  # Chờ tất cả các thread hoàn thành

    return result


if __name__ == "__main__":
    matrix_A = [[1, 2, 3], [4, 5, 6]]
    matrix_B = [[7, 8], [9, 10], [11, 12]]
    C = parallel_multiply_matrices(matrix_A, matrix_B)
    for row in C:
        print(row)
