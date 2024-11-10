import threading
def prefix_sum(arr, result, offset):
    """Tính tổng tiền tố cho một mảng con và lưu kết quả vào result."""
    n = len(arr)
    if n == 0:
        return

    result[0] = arr[0]
    for i in range(1, n):
        result[i] = result[i - 1] + arr[i]

    # Cập nhật giá trị offset cho các phần tử sau
    if offset != 0:
        for i in range(1, n):
            result[i] += offset

def parallel_prefix_sum(arr):
    n = len(arr)
    if n == 0:
        return []

    num_threads = min(4, n)  # Sử dụng tối đa 4 thread hoặc số lượng phần tử
    chunk_size = n // num_threads
    threads = []
    results = [None] * num_threads
    offsets = [0] * num_threads

    # Tạo các thread cho từng phần
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else n
        results[i] = [0] * (end_index - start_index)

        if i > 0:
            offsets[i] = results[i - 1][-1]  # Offset từ phần trước
        thread = threading.Thread(target=prefix_sum, args=(arr[start_index:end_index], results[i], offsets[i]))
        threads.append(thread)
        thread.start()

    # Chờ cho tất cả các thread hoàn thành
    for thread in threads:
        thread.join()

    # Kết hợp kết quả
    final_result = []
    for i in range(num_threads):
        if i > 0:
            # Cộng offset cho phần tử đầu tiên của mỗi phần sau
            results[i][0] += final_result[-1] if final_result else 0
        final_result.extend(results[i])
    return final_result


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
