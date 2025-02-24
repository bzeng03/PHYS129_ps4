import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from a import julia_set  # Import Julia set generation function

# Generate Julia set data
julia_image = julia_set()
height, width = julia_image.shape
xmin, xmax, ymin, ymax = -1.5, 1.5, -1, 1

# Extract points belonging to the Julia set
threshold = 200  # A cutoff for iteration count to identify boundary points
points = np.array([
    [xmin + (x / width) * (xmax - xmin), ymin + (y / height) * (ymax - ymin)]
    for y in range(height) for x in range(width) if julia_image[y, x] > threshold
])

# Compute Convex Hull
hull = ConvexHull(points)

# Plot the Julia set contour and convex hull
plt.figure(figsize=(8, 8))
plt.contourf(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height), julia_image, levels=100, cmap='inferno')
plt.scatter(points[:, 0], points[:, 1], s=1, color='blue', label='Julia Set Points')
for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], 'r-', linewidth=1.5, label='Convex Hull')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.title('Convex Hull on Top of Julia Set Contour')
plt.legend()
plt.show()
plt.savefig("plot_b.png")

# Compute and print the area enclosed by the convex hull
hull_area = hull.volume  # In 2D, volume corresponds to area
print(f'Convex Hull Area: {hull_area}')