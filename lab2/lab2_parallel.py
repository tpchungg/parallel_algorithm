import threading

def multiply(matrix_a, matrix_b, result, index_A, index_B, size):
    for k in range(size):
        result[index_A][index_B] += matrix_a[index_A][k] * matrix_b[k][index_B]

def parallel_multiply_matrices(matrix_a, matrix_b):
    # Kiểm tra kích thước của ma trận
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Số cột của ma trận A phải bằng số hàng của ma trận B.")
    result = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    threads = []
    size = len(matrix_a[0])  # Số cột của matrix_a (cũng là số hàng của matrix_b)

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            thread = threading.Thread(target=multiply, args=(matrix_a, matrix_b, result, i, j, size))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    return result

if __name__ == "__main__":
    matrix_A = [[1, 2, 3], [4, 5, 6]]
    matrix_B = [[7, 8], [9, 10], [11, 12]]
    C = parallel_multiply_matrices(matrix_A, matrix_B)
    for row in C:
        print(row)
