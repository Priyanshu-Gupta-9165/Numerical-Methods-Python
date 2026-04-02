import numpy as np
import sympy as sp

def gauss_jordan(A, b):
    aug = sp.Matrix(np.hstack((A, b.reshape(-1, 1))))
    rref_matrix, _ = aug.rref()
    print("RREF form:\n", rref_matrix)
    solution = [rref_matrix[i, -1] for i in range(rref_matrix.rows)]
    print("Solution:", solution)
    return solution

A1 = np.array([[2, 1],
               [1, -3]], dtype=float)
b1 = np.array([4, 12], dtype=float)

print("2x2 Matrix:")
gauss_jordan(A1, b1)

A2 = np.array([[1, 2, -2],
               [2, 3, 1],
               [2, -1, 4]], dtype=float)
b2 = np.array([7, 10, 8], dtype=float)

print("\n3x3 Matrix:")
gauss_jordan(A2, b2)

A3 = np.array([[1, 1, 2, -1],
               [2, 2, 2, 3],
               [1, -4, -1, 4],
               [2, 3, 3, -2]], dtype=float)
b3 = np.array([2, 4, 3, 5], dtype=float)

print("\n4x4 Matrix:")
gauss_jordan(A3, b3)
