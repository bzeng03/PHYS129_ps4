import numpy as np
import matplotlib.pyplot as plt

# Define function to compute the Julia set
def julia_set(width=800, height=800, xmin=-1.5, xmax=1.5, ymin=-1, ymax=1, c=-0.7 + 0.356j, max_iter=256):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = np.full(Z.shape, c)
    
    output = np.zeros(Z.shape, dtype=int)
    mask = np.ones(Z.shape, dtype=bool)
    
    for i in range(max_iter):
        Z[mask] = Z[mask] ** 2 + C[mask]
        mask = np.abs(Z) < 2
        output[mask] = i
    
    return output

# Generate Julia set
julia_image = julia_set()

# Plot the Julia set
plt.figure(figsize=(8, 8))
plt.imshow(julia_image, cmap='inferno', extent=[-1.5, 1.5, -1, 1])
plt.colorbar(label='Iteration Count')
plt.title('Julia Set for c = -0.7 + 0.356i')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
plt.savefig("plot_a.png")