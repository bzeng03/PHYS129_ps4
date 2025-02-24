import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp
from b import lorenz, sigma, rho, beta, initial_state, t_span, t_eval

# Solve the Lorenz system
solution = solve_ivp(lorenz, t_span, initial_state, args=(sigma, rho, beta), t_eval=t_eval)

# Extract solutions
x, y, z = solution.y

# Create animation
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection='3d')
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_zlim(min(z), max(z))
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Lorenz System Trajectory")

line, = ax.plot([], [], [], lw=1.5, color='blue')

def update(num):
    line.set_data(x[:num], y[:num])
    line.set_3d_properties(z[:num])
    return line,

ani = animation.FuncAnimation(fig, update, frames=len(x), interval=1, blit=False)

# Save the animation
ani.save("lorenz_trajectory.mp4", writer="ffmpeg", fps=30)