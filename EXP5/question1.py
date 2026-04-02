
import numpy as np

def gauss_elimination(A, B):
    n = len(B)
   
    M = np.hstack((A, B.reshape(-1, 1)))
    
    print("\n Initial Augmented Matrix:")
    print(M)

    
   
    for i in range(n):
       
        pivot = M[i][i]
        

        for j in range(i + 1, n):
            factor = M[j][i] / pivot
            M[j] = M[j] - factor * M[i]
            
    print("\n Row Echelon Form:")
    print(M)

    
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = sum(M[i][j] * X[j] for j in range(i + 1, n))
        X[i] = (M[i][n] - sum_ax) / M[i][i]
        
    return X

def main():
  
    
    A = np.array([
        [1.0, 1.0, 1.0],
        [2.0, -3.0, 4.0],
        [3.0, 4.0, 5.0]
    ])
    
    B = np.array([9.0, 10.0, 40.0])
    
    solution = gauss_elimination(A, B)
    
    if solution is not None:
        print("\n Solution:")
        print(f"x = {solution[0]}")
        print(f"y = {solution[1]}")
        print(f"z = {solution[2]}")

if __name__ == "__main__":
    main()
