import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

# --- 1. Definir os parâmetros do circuito ---
R = 10      # Ohms
L = 0.1     # Henry
C = 10e-6   # Farads (10 uF)

# --- 2. Calcular os coeficientes da função de transferência H(s) ---
# H(s) = (s * R/L) / (s^2 + s * R/L + 1/(L*C))

# Coeficientes do numerador: R/L * s + 0
num_H = [R/L, 0]

# Coeficientes do denominador: 1*s^2 + (R/L)*s + (1/(L*C))
den_H = [1, R/L, 1/(L*C)]

# --- 3. Calcular Polos e Zeros de H(s) ---
zeros, poles, gain = tf2zpk(num_H, den_H)

print(f"Zeros de H(s): {zeros}")
print(f"Polos de H(s): {poles}")

# --- 4. Plotar Polos e Zeros ---
plt.figure(figsize=(8, 8))

# Plotar zeros
if len(zeros) > 0:
    plt.plot(np.real(zeros), np.imag(zeros), 'o', markersize=10, label='Zeros', markerfacecolor='none', markeredgecolor='blue')

# Plotar polos
if len(poles) > 0:
    plt.plot(np.real(poles), np.imag(poles), 'x', markersize=10, label='Polos', markeredgecolor='red')

plt.title('Diagrama de Polos e Zeros')
plt.xlabel('Eixo Real')
plt.ylabel('Eixo Imaginário')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.8) # Eixo Real
plt.axvline(0, color='black', linewidth=0.8) # Eixo Imaginário
plt.legend()
plt.axis('equal') # Garante que as escalas dos eixos são iguais para uma visualização correta

plt.savefig('poles_zeros_plot.png')
plt.show()