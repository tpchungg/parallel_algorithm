import threading
import math
import array as arr_module 

def add(a, b, arr, index):
    arr[index] = a + b

def parallel_prefix_sum(a):
    len_a = len(a)
    log_len_a = math.floor(math.log2(len_a))
    b = arr_module.array('i', a)
    for i in range(0, log_len_a + 1):
        step = 2 ** i
        threads = []
        for j in range(step, len_a):
            if len(threads) <= 4:
                for t in threads:
                    t.join()
                threads = []
            t = threading.Thread(target=add, args=(a[j], a[j - step], b, j))
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
        a[:] = b[:]
    return list(b)

if __name__ == '__main__':
    array =list(range(0, 10000))
    print(parallel_prefix_sum(array)[8999])