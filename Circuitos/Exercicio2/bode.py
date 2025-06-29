import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Definir os coeficientes da função de transferência H(s)
# H(s) = 100 / (s^2 + 100s + 10^6)
num = [100]
den = [1, 100, 10**6]

# Criar o objeto da função de transferência
system = signal.TransferFunction(num, den)

# 2. Calcular os dados para o Diagrama de Bode
# Definir um intervalo de frequências para um bom plot (de 10 a 100.000 rad/s)
w_range = np.logspace(1, 5, 500)
w, mag, phase = signal.bode(system, w=w_range)

# 3. Gerar o gráfico
# Define um estilo visual para o gráfico
plt.style.use('seaborn-v0_8-whitegrid')
# Cria a figura com 2 subplots (um para magnitude, um para fase)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# --- Gráfico da Magnitude ---
ax1.semilogx(w, mag, color='red', linewidth=2, label='H(s) Real') # Plota a curva de magnitude
# Linhas de referência que calculamos
ax1.axhline(-80, color='blue', linestyle='--', label='Assíntota Baixa Frequência (-80 dB)')
ax1.axhline(-60, color='green', linestyle='--', label='Pico de Ressonância (-60 dB)')
ax1.axvline(1000, color='purple', linestyle='--', label='Frequência de Canto (1000 rad/s)')
ax1.set_title('Diagrama de Bode: Magnitude', fontsize=14)
ax1.set_ylabel('Magnitude (dB)')
ax1.legend() # Mostra a legenda com os nomes das linhas

# --- Gráfico da Fase ---
ax2.semilogx(w, phase, color='red', linewidth=2) # Plota a curva de fase
# Linhas de referência para fase
ax2.axhline(0, color='gray', linestyle='--')
ax2.axhline(-90, color='orange', linestyle='--', label='Fase em ωn (-90°)')
ax2.axhline(-180, color='gray', linestyle='--')
ax2.axvline(1000, color='purple', linestyle='--')
ax2.set_title('Diagrama de Bode: Fase', fontsize=14)
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.legend() # Mostra a legenda com os nomes das linhas

plt.tight_layout() # Ajusta o espaçamento para não sobrepor os títulos
plt.show() # Mostra o gráfico final