import threading
def prefix_sum(arr, result, offset):
    n = len(arr)
    if n == 0:
        return

    result[0] = arr[0]
    for i in range(1, n):
        result[i] = result[i - 1] + arr[i]  

    for i in range(0, n):
        result[i] += offset

def parallel_prefix_sum(array_a):
    n = len(array_a)
    if n == 0:
        return []

    mid = n // 2
    leftnum = [0] * mid
    rightnum = [0] * (n - mid)

    # Tính tổng tiền tố cho nửa bên trái
    thread_left = threading.Thread(target=prefix_sum, args=(array_a[:mid], leftnum, 0))
    thread_left.start()

    # Tính tổng tiền tố cho nửa bên phải
    thread_right = threading.Thread(target=prefix_sum, args=(array_a[mid:], rightnum, leftnum[-1] if mid > 0 else 0))
    thread_right.start()


    thread_left.join()
    thread_right.join()

    # Kết hợp kết quả
    result = leftnum + rightnum
    return result


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