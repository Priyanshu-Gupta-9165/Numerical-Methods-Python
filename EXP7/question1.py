import numpy as np

def divided_diff(x, y):
    n = len(y)
    coef = np.copy(y)

    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])

    return coef

def newton_poly(coef, x_data, x_val):
    n = len(coef)
    result = coef[n - 1]

    for i in range(n - 2, -1, -1):
        result = result * (x_val - x_data[i]) + coef[i]

    return result

x1 = np.array([1, 2], dtype=float)
y1 = np.array([2, 4], dtype=float)

coef1 = divided_diff(x1, y1)
value1 = newton_poly(coef1, x1, 2.5)

print("2x2 Matrix:")
print("Interpolated value at x = 2.5:", round(value1, 6))

x2 = np.array([2, 1, 4], dtype=float)
y2 = np.array([1, 3, 2], dtype=float)

coef2 = divided_diff(x2, y2)
value2 = newton_poly(coef2, x2, 1.5)

print("\n3x3 Matrix:")
print("Interpolated value at x = 1.5:", round(value2, 6))

x3 = np.array([1, 4, 3, 2], dtype=float)
y3 = np.array([2, 3, 1, 2], dtype=float)

coef3 = divided_diff(x3, y3)
value3 = newton_poly(coef3, x3, 1)

print("\n4x4 Matrix:")
print("Interpolated value at x = 1:", round(value3, 6))
