import numpy as np
import matplotlib.pyplot as plt
from a import julia_set  # Import Julia set generation function

def box_counting(fractal, epsilons):
    counts = []
    size = fractal.shape[0]  # Assume square image
    
    for eps in epsilons:
        num_boxes = int(size / eps)
        count = 0
        
        for i in range(num_boxes):
            for j in range(num_boxes):
                if np.any(fractal[i * eps:(i + 1) * eps, j * eps:(j + 1) * eps] > 0):
                    count += 1
        
        counts.append(count)
    
    return counts

# Generate Julia set
julia_image = julia_set()

# Define epsilon values (box sizes)
epsilons = np.array([2**i for i in range(1, 8)])  # Box sizes from 2^1 to 2^7
counts = box_counting(julia_image, epsilons)

# Compute fractal dimension
log_eps = np.log(1 / epsilons)
log_counts = np.log(counts)
fractal_dim, _ = np.polyfit(log_eps, log_counts, 1)

# Plot box-counting results
plt.figure(figsize=(6, 6))
plt.plot(log_eps, log_counts, 'o-', label=f'Fractal Dimension = {fractal_dim:.4f}')
plt.xlabel('log(1/epsilon)')
plt.ylabel('log(N(epsilon))')
plt.title('Box-Counting Method for Fractal Dimension')
plt.legend()
plt.show()
plt.savefig("plot_d.png")

print(f'Estimated Fractal Dimension: {fractal_dim:.4f}')