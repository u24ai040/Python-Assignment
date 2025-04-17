#QUESTION 6

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2 - x - 2  # Fixed function for now

def bisection(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        print("No sign change found in initial interval. Choose different a and b.")
        return None

    a_values = []
    b_values = []
    mid_values = []

    for i in range(max_iter):
        c = (a + b) / 2.0
        a_values.append(a)
        b_values.append(b)
        mid_values.append(c)

        if abs(f(c)) < tol or abs(b - a) < tol:
            print(f"Root found at x = {c:.5f} after {i+1} iterations.")
            return np.array(mid_values)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Maximum iterations reached.")
    return np.array(mid_values)


try:
    a = float(input("Enter the start of interval (a): "))
    b = float(input("Enter the end of interval (b): "))
    tol=1e-5
    max_iter = int(input("Enter max iterations (e.g., 100): ") or 100)
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()


root_tracking = bisection(f, a, b, tol, max_iter)

x = np.linspace(a, b, 400)
y = f(x)

plt.plot(x, y, label="f(x)")
plt.axhline(0, color='gray', linestyle='--')

if root_tracking is not None:
    plt.plot(root_tracking, f(root_tracking), 'ro-', label="Bisection steps")
    final_root = root_tracking[-1]
    plt.plot(final_root, f(final_root), 'go', label=f"Root ≈ {final_root:.5f}")
    plt.axvline(final_root, color='green', linestyle='--', alpha=0.7)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Bisection Method Root Finding")
plt.legend()
plt.grid(True)
plt.show()
