# Bisection Method with Iteration Table

def f(x):
    return x**3 - 4*x - 9

def bisection_table(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method failed.")
        return

    print("---- Bisection Method for Root Approximation ----\n")
    print("Iter\t a\t\t b\t\t c\t\t f(c)")
    print("----------------------------------------------------------")

    itr = 1
    while (b - a) / 2 > tol:
        c = (a + b) / 2

        print(
            itr, "\t",
            f"{a:.6f}", "\t",
            f"{b:.6f}", "\t",
            f"{c:.6f}", "\t",
            f"{f(c):.6f}"
        )

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        itr += 1

    print("\nApproximate Root =", c)

# Given tolerance and interval
tolerance = 0.0001
bisection_table(2, 3, tolerance)
