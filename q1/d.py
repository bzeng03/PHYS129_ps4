import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

def f(x, r):
    return r * x * (1 - x)

def iterate_logistic_map(x0, r, iterations=1000, discard=100):
    x = x0
    trajectory = []
    for _ in range(discard):  # Discard initial transient values
        x = f(x, r)
    for _ in range(iterations):
        x = f(x, r)
        trajectory.append(x)
    return trajectory

def find_fixed_points(r_values):
    x = symbols('x')
    fixed_points = {}
    
    for r in r_values:
        eq = Eq(x, f(x, r))
        solutions = solve(eq, x)
        fixed_points[r] = [float(sol) for sol in solutions if 0 <= sol <= 1]
    
    return fixed_points

def plot_bifurcation_diagram(r_min=2.4, r_max=4, r_steps=1000, x0=0.2, iterations=500, discard=500):
    r_values = np.linspace(r_min, r_max, r_steps)
    x_values = []
    r_list = []
    
    for r in r_values:
        trajectory = iterate_logistic_map(x0, r, iterations, discard)
        x_values.extend(trajectory)
        r_list.extend([r] * len(trajectory))
    
    plt.figure(figsize=(10, 6))
    plt.scatter(r_list, x_values, s=0.1, color='black', label="Bifurcation")
    
    # Compute and plot fixed points
    fixed_points = find_fixed_points(r_values)
    for r, points in fixed_points.items():
        plt.scatter([r] * len(points), points, s=10, color='red', label="Fixed Points" if r == r_values[0] else "")
    
    plt.xlabel("r")
    plt.ylabel("x")
    plt.title("Bifurcation Diagram of the Logistic Map with Fixed Points")
    plt.legend()
    plt.show()
    plt.savefig("plot_d.png")

# Generate and plot bifurcation diagram with fixed points
plot_bifurcation_diagram()