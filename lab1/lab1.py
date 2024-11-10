import random
import time


# # Random phần tử trong mảng array_a
# def create_random_array(size):
#     return [random.randint(1, 100) for _ in range(size)]


# array_a = create_random_array(1000)
# print(array_a)



# Tính prefix sum
def parallel_prefix_sum(array_a):
    array_b = [0] * len(array_a)
    array_b[0] = array_a[0]      
    for i in range(1, len(array_a)):
        array_b[i] = array_b[i - 1] + array_a[i]
    return array_b


if __name__ == "__main__":
    arr = [random.randint(1, 1) for _ in range(10000)]
    print("Input array:", arr)

    start = time.time()
    result = parallel_prefix_sum(arr)
    print("Prefix sum:", result)
    end = time.time()
    exetime = end - start
    print("Matrix exetime: ", exetime)
