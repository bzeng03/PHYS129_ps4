import numpy as np
import matplotlib.pyplot as plt

def modified_logistic_map(x, r, gamma):
    return r * x * (1 - x**gamma)

def find_first_bifurcation(r_min, r_max, gamma, x0=0.2, iterations=100, discard=500):
    r_values = np.linspace(r_min, r_max, 500)
    bifurcation_points = []
    
    for r in r_values:
        x = x0
        trajectory = []
        for _ in range(discard):
            x = modified_logistic_map(x, r, gamma)
        for _ in range(iterations):
            x = modified_logistic_map(x, r, gamma)
            trajectory.append(x)
        
        unique_values = np.unique(np.round(trajectory[-100:], 5))
        if len(unique_values) > 1:
            bifurcation_points.append((gamma, r))
            break
    
    return bifurcation_points

def plot_first_bifurcation_vs_gamma(gamma_min=0.5, gamma_max=1.5, gamma_steps=1000, r_min=0, r_max=4):
    gamma_values = np.linspace(gamma_min, gamma_max, gamma_steps)
    bifurcation_values = []
    
    for gamma in gamma_values:
        bifurcation_point = find_first_bifurcation(r_min, r_max, gamma)
        if bifurcation_point:
            bifurcation_values.append(bifurcation_point[0])
    
    if bifurcation_values:
        gamma_vals, r_vals = zip(*bifurcation_values)
        plt.figure(figsize=(8, 5))
        plt.scatter(gamma_vals, r_vals, color='blue')
        plt.xlabel("Gamma (γ)")
        plt.ylabel("First Bifurcation Point (r)")
        plt.title("First Bifurcation Point as a Function of γ")
        plt.show()
        plt.savefig("plot_e.png")

# Plot the first bifurcation point vs. gamma
plot_first_bifurcation_vs_gamma()