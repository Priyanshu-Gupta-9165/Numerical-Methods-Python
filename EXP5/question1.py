
import numpy as np

def gauss_elimination(A, B):
    n = len(B)
    # Augmented matrix
    M = np.hstack((A, B.reshape(-1, 1)))
    
    print("Initial Augmented Matrix:")
    print(M)
    print("-" * 20)
    
    # Forward Elimination
    for i in range(n):
        
        # Taking pivot
        pivot = M[i][i]
        
        if pivot == 0:
            print("Pivot is zero, simple Gauss elimination fails or requires swapping.")
            return None

        for j in range(i + 1, n):
            factor = M[j][i] / pivot
            M[j] = M[j] - factor * M[i]
            
    print("Row Echelon Form:")
    print(M)
    print("-" * 20)

    # Back Substitution
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = sum(M[i][j] * X[j] for j in range(i + 1, n))
        X[i] = (M[i][n] - sum_ax) / M[i][i]
        
    return X

def main():
    # System of equations:
    # x + y + z = 9
    # 2x - 3y + 4z = 10
    # 3x + 4y + 5z = 40
    
    A = np.array([
        [1.0, 1.0, 1.0],
        [2.0, -3.0, 4.0],
        [3.0, 4.0, 5.0]
    ])
    
    B = np.array([9.0, 10.0, 40.0])
    
    solution = gauss_elimination(A, B)
    
    if solution is not None:
        print("Solution:")
        print(f"x = {solution[0]}")
        print(f"y = {solution[1]}")
        print(f"z = {solution[2]}")

if __name__ == "__main__":
    main()
