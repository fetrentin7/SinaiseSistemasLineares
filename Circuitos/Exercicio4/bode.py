import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# --- 1. Definição da Função de Transferência ---
# H(s) = (s^2 + 1.000.000) / (s^2 + 100s + 1.000.000)
num = [1, 0, 1000000]
den = [1, 900, 1000000]
sistema = sig.TransferFunction(num, den)

# Frequência de corte (natural)
w_c = 1000

# --- 2. Cálculo da Resposta em Frequência ---
# Gera um range de frequências em escala logarítmica
# Aumentamos os pontos para capturar bem o "notch"
frequencias = np.logspace(1, 5, 10000)
w, mag, phase = sig.bode(sistema, frequencias)

# --- 3. Plotagem do Diagrama de Bode ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# --- Gráfico de Magnitude ---
ax1.semilogx(w, mag, color='blue', label='Curva Real')
ax1.set_title('Diagrama de Bode: Magnitude', fontsize=16)
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(True, which='both')

# Plotando as Assíntotas de Magnitude
# A assíntota é uma linha reta em 0 dB, pois o ganho em baixa e alta frequência é 1.
ax1.plot(w, np.zeros_like(w), 'r--', label='Assíntotas (0 dB)')
ax1.legend()
# Marca a frequência do notch
ax1.axvline(w_c, color='g', linestyle=':', label=f'ω = {w_c} rad/s')


# --- Gráfico de Fase ---
ax2.semilogx(w, phase, color='green', label='Curva de Fase')
ax2.set_title('Diagrama de Bode: Fase', fontsize=16)
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.grid(True, which='both')
# Marca a frequência do notch
ax2.axvline(w_c, color='g', linestyle=':')

plt.tight_layout() # Ajusta o espaçamento entre os gráficos
plt.show()