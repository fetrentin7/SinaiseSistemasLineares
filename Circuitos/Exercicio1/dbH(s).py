import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ---  Definição da Função de Transferência e seus Componentes ---

# H(s) Total = s / (s + 100)
sistema_total = signal.TransferFunction([1, 0], [1, 100])

# Componente 1: Ganho Constante, K = 1/100
sistema_K = signal.TransferFunction([1], [100])

# Componente 2: Zero na origem, H_zero(s) = s
sistema_Z = signal.TransferFunction([1, 0], [1])

# Componente 3: Polo normalizado em 100 rad/s, H_polo(s) = 100 / (s + 100)
sistema_P = signal.TransferFunction([100], [1, 100])


# --- Dados do Diagrama de Bode ---
frequencias = np.logspace(-3, 4, 1000)

w, mag_total, phase_total = signal.bode(sistema_total, w=frequencias)
w, mag_K, phase_K = signal.bode(sistema_K, w=frequencias)
w, mag_Z, phase_Z = signal.bode(sistema_Z, w=frequencias)
w, mag_P, phase_P = signal.bode(sistema_P, w=frequencias)


# --- 3. Soma manual dos componentes (em dB e graus) ---
mag_soma = mag_K + mag_Z + mag_P
phase_soma = phase_K + phase_Z + phase_P


# --- 4. Plotagem do Gráfico Combinado ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
fig.suptitle("Decomposição do Diagrama de Bode", fontsize=14)

# --- Gráfico da Magnitude ---
ax1.semilogx(w, mag_K, linestyle='-.', color='gray', label='Ganho K = 1/100 (-40 dB)')
ax1.semilogx(w, mag_Z, linestyle='--', color='green', label='Zero na Origem (s)')
ax1.semilogx(w, mag_P, linestyle='--', color='purple', label='Polo em -100')
ax1.semilogx(w, mag_soma, linestyle=':', color='black', linewidth=3, label='Soma das Assíntotas')
ax1.semilogx(w, mag_total, color='red', linewidth=2, alpha=0.8, label='H(s) Total (Curva Real)')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title('Análise da Magnitude')
ax1.grid(True, which='both')
ax1.legend()
ax1.set_ylim(-80, 60) # Ajustando o zoom do eixo Y

# --- Gráfico da Fase ---
ax2.semilogx(w, phase_K, linestyle='-.', color='gray', label='Ganho K (0°)')
ax2.semilogx(w, phase_Z, linestyle='--', color='green', label='Zero na Origem (+90°)')
ax2.semilogx(w, phase_P, linestyle='--', color='purple', label='Polo em -100 (0° a -90°)')
ax2.semilogx(w, phase_soma, linestyle=':', color='black', linewidth=3, label='Soma das Fases')
ax2.semilogx(w, phase_total, color='red', linewidth=2, alpha=0.8, label='H(s) Total (Curva Real)')
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.set_title('Análise da Fase')
ax2.grid(True, which='both')
ax2.legend()
6
plt.show()