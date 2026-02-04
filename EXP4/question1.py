import math

print("----- Regula–Falsi (False Position) Method for Root Estimation (Question 1) -----")
print("Function: f(x) = x^3 - x - 2")

# Define the function
def f(x):
    return x**3 - x - 2

# Regula–Falsi Method
def regula_falsi(a, b, tol=1e-6, max_iter=50):
    if f(a) * f(b) >= 0:
        print("Invalid interval: No sign change.")
        return None
    
    print(f"\n{'Iter':<5} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12}")
    
    for i in range(1, max_iter + 1):
        # Formula for c
        # Avoid division by zero
        denom = f(b) - f(a)
        if denom == 0:
            print("Division by zero error.")
            return None
            
        c = b - (f(b) * (b - a)) / denom
        fc = f(c)
        
        print(f"{i:<5} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6f}")
        
        # Check convergence
        if abs(fc) < tol:
            return c
        
        # Update the interval based on sign change
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return c

# Initial interval
# f(1) = 1 - 1 - 2 = -2
# f(2) = 8 - 2 - 2 = 4
# Sign change exists between 1 and 2
a = 1
b = 2
print(f"\nInitial Interval: [{a}, {b}]")

# Calling the function
root = regula_falsi(a, b)
print("\nApproximate Root =", root)
