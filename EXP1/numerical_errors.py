from decimal import Decimal, getcontext
import math

getcontext().prec = 25

a = 0.1
b = 0.2
c = 0.3

sum1 = a + b - c

a1 = Decimal('0.1')
b1 = Decimal('0.2')
c1 = Decimal('0.3')

sum2 = a1 + b1 - c1

error = Decimal(sum1) - sum2

print("Round-Off Error")
print("Approximate Value:", sum1)
print("Exact Value:", sum2)
print("Error:", error)


x = 2
exact_exp = math.exp(x)
approx_exp = 1 + x + (x**2)/2

trunc_error_exp = exact_exp - approx_exp

print("\nTruncation Error for e^x")
print("Exact Value:", exact_exp)
print("Approx Value:", approx_exp)
print("Truncation Error:", trunc_error_exp)


y = math.pi / 6

exact_sin = math.sin(y)
approx_sin = y - (y**3)/6

print("\nTruncation Error for sin(x)")
print("Exact Value:", exact_sin)
print("Approx Value:", approx_sin)
print("Error:", exact_sin - approx_sin)


def taylor_sin(x, terms):
    s = 0
    for i in range(terms):
        power = 2*i + 1
        s += ((-1)**i) * (x**power) / math.factorial(power)
    return s

print("\nTerms\tApprox Value\tTruncation Error")
exact = math.sin(y)

for t in [2, 4, 6, 8]:
    approx = taylor_sin(y, t)
    error = abs(exact - approx)
    print(f"{t}\t{approx:.10f}\t{error:.10f}")
