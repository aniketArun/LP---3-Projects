import threading
import numpy as np
import time

# Generate random matrices
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

def multiply_row(A, B, C, row):
    n, m = A.shape
    m, p = B.shape
    for j in range(p):
        C[row][j] = sum(A[row][k] * B[k][j] for k in range(m))

def matrix_multiply_multithreaded_row(A, B):
    n, _ = A.shape
    _, p = B.shape
    C = np.zeros((n, p))
    
    threads = []
    for i in range(n):
        thread = threading.Thread(target=multiply_row, args=(A, B, C, i))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return C

# Measure time taken for multithreaded multiplication (one thread per row)
start_time = time.time()
C_multithreaded_row = matrix_multiply_multithreaded_row(A, B)
end_time = time.time()

print(f"Multithreaded Row-wise Matrix Multiplication Time: {end_time - start_time:.6f} seconds")
