import numpy as np

def f(x, r):
    return r * x * (1 - x)

def iterate_logistic_map(x0, f, r, e, depth=0, max_depth=1000):
    if depth > max_depth:
        raise RecursionError("The logistic map does not converge")
    if np.abs(x0 - f(x0, r)) > e:
        return iterate_logistic_map(f(x0, r), f, r, e, depth + 1)
    return round(x0, 2)

# Iterating logistic map with recursion depth check
x0 = 0.2
e = 1e-6
r_values = [2, 3, 3.5, 3.8, 4]

for r in r_values:
    print(f"For r = {r}:")
    try:
        print(f"Fix Point: f(x0) converges to: {iterate_logistic_map(x0, f, r, e)} with convergence threshold {e}")
    except RecursionError as ex:
        print(f"Recursion error: {ex}. The logistic map does not converge.")
    print("\n")
