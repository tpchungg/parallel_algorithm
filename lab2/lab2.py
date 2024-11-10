def multiply_matrices(matrix_A, matrix_B):
    if len(matrix_A[0]) != len(matrix_B):
        raise ValueError("Số cột của ma trận matrix_A phải bằng số hàng của ma trận matrix_B.")

    result = [[0 for _ in range(len(matrix_B[0]))] for _ in range(len(matrix_A))]

    # Nhân ma trận
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]

    return result

if __name__ == "__main__":
    matrix_A = [[1, 2, 3],
        [4, 5, 6]]
    matrix_B = [[7, 8],
        [9, 10],
        [11, 12]]
    C = multiply_matrices(matrix_A, matrix_B)
    for row in C:
        print(row)
