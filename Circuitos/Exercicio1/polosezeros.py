
import matplotlib.pyplot as plt

# Polo e zero
zero = 0
R = 1000  # Ohms
C = 10e-6  # Farads
polo = -1 / (R * C)

# Gráfico
plt.figure(figsize=(6, 6))
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)

# Plotar zero (x) e polo (o)
plt.plot(zero, 0, 'bx', markersize=12, label='Zero em s = 0')
plt.plot(polo, 0, 'ro', markersize=10, label=f'Polo em s = {int(polo)}')

plt.title("Diagrama de Polos e Zeros de H(s) = s / (s + 1/RC)")
plt.xlabel("Parte Real")
plt.ylabel("Parte Imaginária")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()