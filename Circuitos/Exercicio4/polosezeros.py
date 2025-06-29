import matplotlib.pyplot as plt
import numpy as np

# Define the poles and zeros
# Zeros are roots of the numerator: s^2 + 1,000,000 = 0 => s = +-j1000
zeros = [0 + 1000j, 0 - 1000j]

# Poles are roots of the denominator: s^2 + 100s + 1,000,000 = 0
# Using the quadratic formula: s = (-b +- sqrt(b^2 - 4ac)) / 2a
# a = 1, b = 100, c = 1,000,000
# Discriminant = b^2 - 4ac = 100^2 - 4 * 1 * 1,000,000 = 10000 - 4000000 = -3990000
# sqrt(-3990000) = j * sqrt(3990000) = j * 1997.49843689
# s1 = (-100 + j * 1997.49843689) / 2 = -50 + j998.749218445
# s2 = (-100 - j * 1997.49843689) / 2 = -50 - j998.749218445
poles = [-50 + 998.749218445j, -50 - 998.749218445j]

# Create the plot
plt.figure(figsize=(8, 8))

# Plot the zeros as circles
for z in zeros:
    plt.plot(z.real, z.imag, 'o', markersize=10, color='blue', label='Zeros' if 'Zeros' not in plt.gca().get_legend_handles_labels()[1] else "")

# Plot the poles as 'x' marks
for p in poles:
    plt.plot(p.real, p.imag, 'x', markersize=10, color='red', label='Poles' if 'Poles' not in plt.gca().get_legend_handles_labels()[1] else "")

# Add labels and title
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.title('Pole-Zero Plot')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.axis('equal') # Ensures equal scaling for x and y axes
plt.show()