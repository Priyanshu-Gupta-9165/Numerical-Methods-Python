import math

print("----- Newton–Raphson Method for Root Approximation (Question 1) -----")
print("Function: f(x) = x^3 - x - 2")

# Define function
def f(x):
    return x**3 - x - 2

# Define derivative
def df(x):
    return 3*x**2 - 1

# Newton–Raphson Method
def newton_raphson(x0, tol=1e-6, max_iter=20):
    print(f"\n{'Iter':<5} {'x_n':<12} {'f(x_n)':<12}")
    for i in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Derivative is zero. Method fails.")
            return None

        print(f"{i:<5} {x0:<12.6f} {fx:<12.6f}")

        # Newton-Raphson formula
        x1 = x0 - fx / dfx

        # Check for convergence
        if abs(x1 - x0) < tol:
            return x1
        
        x0 = x1

    return x0

# Initial guess
x0 = 1.5
print(f"\nInitial Guess x0 = {x0}")
root = newton_raphson(x0)
print("\nApproximate Root =", root)
