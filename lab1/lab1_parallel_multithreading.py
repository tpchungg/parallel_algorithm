import concurrent.futures
import math

def add(a, b):
    return a + b
def parallel_prefix_sum(a):
    len_a = len(a)
    b = a[:]  # Tạo một bản sao của danh sách a
    log_len_a = math.floor(math.log2(len_a))
    for i in range(log_len_a + 1):
        step = 2 ** i
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for j in range(step, len_a):
                futures.append(executor.submit(add, b[j], b[j - step]))
            for j, future in enumerate(futures, start=step):
                b[j] = future.result()
        a[:] = b[:]  # Cập nhật mảng a bằng mảng b
    return b  # Trả về danh sách b

import time
import random
if __name__ == "__main__":
    arr = [random.randint(1, 1) for _ in range(10000)]
    print("Input array:", arr)
    start = time.time()
    result = parallel_prefix_sum(arr)
    print("Prefix sum:", result)
    end = time.time()
    exetime = end - start
    print("Matrix exetime: ", exetime)
