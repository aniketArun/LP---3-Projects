import numpy as np
import time

def matrix_multiply(A, B):
    # Get dimensions
    n, m = A.shape
    m, p = B.shape
    # Resultant matrix
    C = np.zeros((n, p))
    
    for i in range(n):
        for j in range(p):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(m))
    return C

# Generate random matrices
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

# Measure time taken for standard multiplication
start_time = time.time()
C_standard = matrix_multiply(A, B)
end_time = time.time()

print(f"Standard Matrix Multiplication Time: {end_time - start_time:.6f} seconds")
