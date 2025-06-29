import numpy as np
import matplotlib.pyplot as plt

# Valores de R e C
R = 1000  # Ohms
C_values = [100e-6, 10e-6]  # Farads: 100uF e 10uF

# Tempo
t = np.linspace(0, 0.5, 1000)
x_t = 2 * np.ones_like(t)  # Entrada: 2u(t)

# Plotagem
plt.figure(figsize=(10, 6))
for C in C_values:
    RC = R * C
    y_t = 2 * np.exp(-t / RC)
    plt.plot(t, y_t, label=f'C = {int(C*1e6)} μF')

plt.plot(t, x_t, '--', label='Entrada x(t) = 2u(t)', color='gray')
plt.title("Saída y(t) = 2e^(-t/RC) para diferentes valores de C (R = 1kΩ)")
plt.xlabel("Tempo (s)")
plt.ylabel("Tensão (V)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()