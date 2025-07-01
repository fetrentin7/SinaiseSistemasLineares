import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Definir os coeficientes da função de transferência H(s)
# H(s) = 100 / (s^2 + 100s + 10^6)
num = [100]
den = [1, 100, 10**6]
system = signal.TransferFunction(num, den)

# Frequência de canto e ganho DC
wn = 1000
low_freq_gain_db = 20 * np.log10(num[0] / den[2]) # -80 dB

# 2. Calcular os dados para o Diagrama de Bode
w_range = np.logspace(1, 5, 500)
w, mag, phase = signal.bode(system, w=w_range)


# --- Cálculo das Assíntotas ---

# Assíntota de Magnitude (plana em -80dB, depois caindo a -40dB/dec)
mag_asymptote = np.piecewise(w,
    [w < wn],
    [low_freq_gain_db, lambda w: low_freq_gain_db - 40 * (np.log10(w) - np.log10(wn))]
)

# Assíntota de Fase (de 0 a -180 graus)
start_freq_phase = wn / 10
end_freq_phase = wn * 10
phase_asymptote = np.piecewise(w,
    [w < start_freq_phase, (w >= start_freq_phase) & (w < end_freq_phase), w >= end_freq_phase],
    [0, lambda w: -90 * (np.log10(w) - np.log10(start_freq_phase)), -180]
)


# 3. Gerar o gráfico
plt.style.use('seaborn-v0_8-whitegrid')
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# --- Gráfico da Magnitude ---
ax1.semilogx(w, mag, color='red', linewidth=2.5, label='H(s) Real', zorder=5)
ax1.semilogx(w, mag_asymptote, color='k', linestyle='-.', label='Assíntota de Reta', zorder=4)

ax1.axhline(-80, color='blue', linestyle='--', label='Ganho Baixa Frequência (-80 dB)')
ax1.axhline(-60, color='green', linestyle='--', label='Nível do Pico Aprox. (-60 dB)')
ax1.axvline(1000, color='purple', linestyle='--', label='Frequência de Canto (1000 rad/s)')

ax1.set_title('Diagrama de Bode: Magnitude', fontsize=14)
ax1.set_ylabel('Magnitude (dB)')
ax1.legend()

# --- Gráfico da Fase ---
ax2.semilogx(w, phase, color='red', linewidth=2.5, label='H(s) Real', zorder=5)
ax2.semilogx(w, phase_asymptote, color='k', linestyle='-.', label='Assíntota de Fase', zorder=4)
ax2.axhline(-90, color='orange', linestyle='--', label='Fase em ωn (-90°)')
ax2.axvline(wn, color='purple', linestyle='--', label=f'ωn = {wn} rad/s')
ax2.set_title('Diagrama de Bode: Fase', fontsize=14)
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.legend()

plt.tight_layout()
plt.show()