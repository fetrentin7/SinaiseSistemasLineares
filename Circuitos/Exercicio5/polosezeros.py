import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


numerador = [50_000]

denominador = [1, 500, 50_000]


sistema = signal.TransferFunction(numerador, denominador)
polos = sistema.poles
zeros = sistema.zeros


print(f" H(s) = {sistema}")
print("---------------------------------")
print(f" Polos: {np.round(polos, 4)}") # Rounding for better readability
print(f" Zeros: {np.round(zeros, 4)}") # Rounding for better readability



plt.figure(figsize=(8, 8))


plt.scatter(np.real(polos), np.imag(polos), s=150, marker='x', color='red', label='Poles')


if len(zeros) > 0:
    plt.scatter(np.real(zeros), np.imag(zeros), s=150, marker='o',
                facecolors='none', edgecolors='blue', linewidths=1.5, label='Zeros')

# Configure plot for clarity
plt.axhline(0, color='black', lw=1) # Horizontal axis
plt.axvline(0, color='black', lw=1) # Vertical axis
plt.grid(True, linestyle='--', alpha=0.6)

# Add titles, legends, and axis labels
plt.title('Pole-Zero Diagram', fontsize=16)
plt.xlabel(r'Real Axis ($\sigma$)', fontsize=12)
plt.ylabel(r'Imaginary Axis ($j\omega$)', fontsize=12)
plt.legend(fontsize=12)


max_abs_pole = max(abs(p) for p in polos) if polos.size > 0 else 1000 # Default if no poles
plot_limit = max_abs_pole * 1.1 # Add a 10% buffer
plt.xlim(-plot_limit, plot_limit)
plt.ylim(-plot_limit, plot_limit)

plt.axis('equal') # Ensures equal scaling for x and y axes

plt.show()