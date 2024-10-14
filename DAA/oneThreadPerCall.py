import threading
import numpy as np
import time

# Generate random matrices
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

def multiply_cell(A, B, C, row, col):
    n, m = A.shape
    m, p = B.shape
    C[row][col] = sum(A[row][k] * B[k][col] for k in range(m))

def matrix_multiply_multithreaded_cell(A, B):
    n, _ = A.shape
    _, p = B.shape
    C = np.zeros((n, p))
    
    threads = []
    for i in range(n):
        for j in range(p):
            thread = threading.Thread(target=multiply_cell, args=(A, B, C, i, j))
            threads.append(thread)
            thread.start()
    
    for thread in threads:
        thread.join()
    
    return C

# Measure time taken for multithreaded multiplication (one thread per cell)
start_time = time.time()
C_multithreaded_cell = matrix_multiply_multithreaded_cell(A, B)
end_time = time.time()

print(f"Multithreaded Cell-wise Matrix Multiplication Time: {end_time - start_time:.6f} seconds")
