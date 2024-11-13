from multiprocessing import Process, Manager, Queue
import math

def multiply(matrix_a,matrix_b,i,j,z,dim):
  # không sử dụng parallel vì quas nhiều process dễ gây lỗi
  for k in range(dim):
    z[i][j]+=matrix_a[i][k]*matrix_b[k][j]


def parallel_multiply_matrices(matrix_a, matrix_b):
  dim=len(matrix_a)
  manager = Manager()
  z =manager.list([manager.list([0] *dim) for _ in range(dim)])
  process=[]
  for i in range(0,dim):
    for j in range(0,dim):
      p = Process(target=multiply, args=(matrix_a,matrix_b,i,j,z,dim))
      process.append(p)
      p.start()
      if len(process)>=3:
        for p in process:
          p.join()
        process=[]
  for p in process:
    p.join()
  return z

def pow_matrix(matrix,n):
  if n==1:
    return matrix
  if not n%2:
    temp=pow_matrix(matrix,n//2)
    return parallel_multiply_matrices(temp,temp)
  else:
    temp=pow_matrix(matrix,n//2)
    return parallel_multiply_matrices(parallel_multiply_matrices(temp,temp),matrix)
#f(2k)=(f(k+1)−f(k-1))*f(k) số chẵn
#f(2k+1)=f(k+1)^2+f(k)^2 số lẻ
def fibonacci(n):
  matrix_base=[[1,1],[1,0]]
  k=math.floor(n/2)
  matrix_k=pow_matrix(matrix_base,k)
  if not n%2:
    result=(matrix_k[1][1]+matrix_k[0][0])*matrix_k[1][0]
  else:
    result=matrix_k[0][0]**2+matrix_k[0][1]**2
  return result


if __name__ == '__main__':
    print(fibonacci(9999))