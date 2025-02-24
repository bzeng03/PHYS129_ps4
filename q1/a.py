import numpy as np
from sympy import symbols, Eq, solve, diff

def f(x, r):
    return r * x * (1 - x)

def f_prime(x, r):
    return r * (1 - 2 * x)

def find_fixed_points(r_values):
    global f, f_prime
    x = symbols('x')
    results = {}
    
    for r in r_values:
        # Define the equation x = f(x, r)
        eq = Eq(x, f(x, r))
        fixed_points = solve(eq, x)
        
        stability = {}
        
        for point in fixed_points:
            # Evaluate derivative at fixed points
            stability[point] = f_prime(point, r)
            
        results[r] = {"Fixed Points": fixed_points, "Stability": stability}
    
    return results

# Define r values to test
r_values = [1, 2, 3, 4]

# Compute fixed points and stability
results = find_fixed_points(r_values)

# Print results
for r, data in results.items():
    print(f"For r = {r}:")
    for point, derivative in data["Stability"].items():
        stability_type = "Stable" if abs(derivative) < 1 else "Unstable"
        print(f"  Fixed Point: {point}, f'(x) = {derivative}, Stability: {stability_type}")
    print("\n")
