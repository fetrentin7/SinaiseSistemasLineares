import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- 1. Definição da Função de Transferência Total ---
# H(s) = (s + 1000) / [(s + 114.92)(s + 435.08)]
# Primeiramente, definimos o sistema com polos, zeros e ganho
zeros = [-1000]
polos = [-435.08, -114.92]
ganho_k = 1
# Convertemos para a forma polinomial para o objeto principal
numerador_total, denominador_total = signal.zpk2tf(zeros, polos, ganho_k)
sistema_total = signal.TransferFunction(numerador_total, denominador_total)


# --- 2. Definição dos Componentes Individuais para o Bode ---

# Componente de Ganho K
ganho_K_valor = 1000 / (114.92 * 435.08)
sistema_K = signal.TransferFunction([ganho_K_valor], [1])

# Componente do Zero em s = -1000 (normalizado)
sistema_Z = signal.TransferFunction([1/1000, 1], [1])

# Componente do Polo 1 em s = -114.92 (normalizado)
sistema_P1 = signal.TransferFunction([1], [1/114.92, 1])

# Componente do Polo 2 em s = -435.08 (normalizado)
sistema_P2 = signal.TransferFunction([1], [1/435.08, 1])


# --- 3. Cálculo dos Dados do Diagrama de Bode ---
frequencias = np.logspace(1, 5, 1000) # De 10 a 100k rad/s

w, mag_total, phase_total = signal.bode(sistema_total, w=frequencias)
w, mag_K, phase_K = signal.bode(sistema_K, w=frequencias)
w, mag_Z, phase_Z = signal.bode(sistema_Z, w=frequencias)
w, mag_P1, phase_P1 = signal.bode(sistema_P1, w=frequencias)
w, mag_P2, phase_P2 = signal.bode(sistema_P2, w=frequencias)


# --- 4. Soma manual de TODOS os componentes ---
mag_soma = mag_K + mag_Z + mag_P1 + mag_P2
phase_soma = phase_K + phase_Z + phase_P1 + phase_P2


# --- 5. Plotagem do Gráfico Combinado ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
fig.suptitle("Decomposição do Bode: H(s) = (s+1000)/[(s+114.92)(s+435.08)]", fontsize=14)

# --- Gráfico da Magnitude ---
ax1.semilogx(w, mag_K, linestyle='-.', color='gray', label=f'Ganho K ≈ {ganho_K_valor:.2f} ({mag_K[0]:.1f} dB)')
ax1.semilogx(w, mag_Z, linestyle='--', color='green', label='Zero em -1000')
ax1.semilogx(w, mag_P1, linestyle='--', color='purple', label='Polo em -114.92')
ax1.semilogx(w, mag_P2, linestyle='--', color='orange', label='Polo em -435.08')
ax1.semilogx(w, mag_soma, linestyle=':', color='black', linewidth=3, label='Soma dos Componentes (Assíntota)')
ax1.semilogx(w, mag_total, color='red', linewidth=2, alpha=0.8, label='H(s) Total (Curva Real)')
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title('Análise da Magnitude (Ganho)')
ax1.grid(True, which='both')
ax1.legend()

# --- Gráfico da Fase ---
ax2.semilogx(w, phase_Z, linestyle='--', color='green', label='Fase do Zero')
ax2.semilogx(w, phase_P1, linestyle='--', color='purple', label='Fase do Polo 1')
ax2.semilogx(w, phase_P2, linestyle='--', color='orange', label='Fase do Polo 2')
ax2.semilogx(w, phase_soma, linestyle=':', color='black', linewidth=3, label='Soma das Fases')
ax2.semilogx(w, phase_total, color='red', linewidth=2, alpha=0.8, label='H(s) Total')
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.set_title('Análise da Fase')
ax2.grid(True, which='both')
ax2.legend()

plt.show()