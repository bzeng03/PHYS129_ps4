import numpy as np
import matplotlib.pyplot as plt

def f(x, r):
    return r * x * (1 - x)

def iterate_logistic_map(x0, f, r, e, depth=0, max_depth=1000):
    if depth > max_depth:
        raise RecursionError("The logistic map does not converge")
    if np.abs(x0 - f(x0, r)) > e:
        return iterate_logistic_map(f(x0, r), f, r, e, depth + 1)
    return round(x0, 2)

def plot_logistic_map_different_x0(r_values, x0_values, e, iterations=100):
    fig, axes = plt.subplots(len(r_values), 1, figsize=(8, 5 * len(r_values)))
    
    for ax, r in zip(axes, r_values):
        for x0 in x0_values:
            x = x0
            series = []
            for _ in range(iterations):
                x = f(x, r)
                series.append(x)
            ax.plot(range(iterations), series, label=f'x0 = {x0}')
        
        ax.set_xlabel('Iterations')
        ax.set_ylabel('x')
        ax.set_title(f'Logistic Map Time Series for r = {r}')
        ax.legend()
    
    plt.tight_layout()
    plt.show()
    plt.savefig("plot_c.png")

# Define parameters
r_values = [2, 3, 3.5, 3.8, 4]
x0_values = [0.1, 0.2, 0.3, 0.5]
e = 1e-6

# Plot time series for different initial conditions
plot_logistic_map_different_x0(r_values, x0_values, e)