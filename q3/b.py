import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lorenz system
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Set parameters
sigma = 10
rho = 48
beta = 3

# Initial conditions
initial_state = [1.0, 1.0, 1.0]

# Time range
t_span = (0, 12)
t_eval = np.linspace(t_span[0], t_span[1], 5000)  # Generate time points

# Solve the Lorenz system
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Extract solutions
x, y, z = solution.y

# Plot the Lorenz attractor
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z, lw=0.5, color='blue')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz Attractor")
plt.show()
plt.savefig("plot_b.png")
