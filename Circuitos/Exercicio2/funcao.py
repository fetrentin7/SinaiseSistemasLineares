import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk # Importar para polos e zeros

# --- 1. Definir os parâmetros do circuito (valores corrigidos) ---
R = 10      # Ohms
L = 0.1     # Henry
C = 10e-6   # Farads (10 uF)

# --- 2. Calcular os coeficientes da função de transferência H(s) ---
# H(s) = (s * R/L) / (s^2 + s * R/L + 1/(L*C))
num_H = [R/L, 0]  # Numerador: [100, 0] -> 100s
den_H = [1, R/L, 1/(L*C)] # Denominador: [1, 100, 10^6] -> s^2 + 100s + 10^6

print(f"Coeficientes do numerador de H(s): {num_H}")
print(f"Coeficientes do denominador de H(s): {den_H}")
print("-" * 30)

# --- 3. Calcular Polos e Zeros de H(s) ---
zeros, poles, gain = tf2zpk(num_H, den_H)

print(f"Zeros de H(s): {zeros}")
print(f"Polos de H(s): {poles}")
print(f"Ganho de H(s): {gain}") # Este é o ganho de H(s) na forma ZPK
print("-" * 30)

# --- 4. Definir a entrada x(t) = 2u(t) ---
# No domínio de Laplace, X(s) = 2/s.
# A entrada no tempo é uma função degrau de amplitude 2.

# --- 5. Definir os parâmetros para a plotagem da saída y(t) ---
# Re-calculando os parâmetros com base nos polos para garantir consistência
# Polos: -50 +/- j998.7495
alpha = np.real(poles[0]) # Parte real de um dos polos
omega_d = np.abs(np.imag(poles[0])) # Parte imaginária (frequência de oscilação)

# Para a amplitude da saída, precisamos dos coeficientes A e B.
# Y(s) = 200 / (s^2 + 100s + 10^6)
# Y(s) = 200 / ((s - s1)(s - s2))
# A = 200 / (s1 - s2)
s1 = poles[0]
s2 = poles[1]
A_coeff = 200 / (s1 - s2)
amplitude_y = 2 * np.abs(A_coeff) # 2 * |C| na fórmula da transformada inversa

print(f"Parâmetros da Saída y(t):")
print(f"  Alfa (decaimento): {alpha:.4f}")
print(f"  Ômega_d (frequência de oscilação): {omega_d:.4f} rad/s")
print(f"  Amplitude da senoide amortecida: {amplitude_y:.4f}")
print("-" * 30)


# Definir o tempo de simulação
t_end = 0.05 # Tempo final (suficiente para ver o transiente e algumas oscilações)
num_points = 500 # Número de pontos para a plotagem
t = np.linspace(0, t_end, num_points)

# Calcular a entrada x(t)
x_t = 2 * np.ones_like(t) # Função degrau unitário com amplitude 2

# Calcular a saída y(t)
y_t = amplitude_y * np.exp(alpha * t) * np.sin(omega_d * t) # O faseamento já está embutido no sin(omega_d * t) quando A é puramente imaginário

# --- 6. Plotar os resultados ---
plt.figure(figsize=(10, 6))

plt.plot(t, x_t, label='Entrada x(t) = 2u(t)', linestyle='--', color='blue')
plt.plot(t, y_t, label='Saída y(t)', color='red')

plt.title('Resposta do Circuito RL-C à Entrada Degrau')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5) # Linha de referência no zero
plt.legend()
plt.show()