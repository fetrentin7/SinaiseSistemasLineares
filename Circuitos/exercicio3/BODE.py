import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Definições Iniciais ---
w = np.logspace(-1, 5, 1000)
w1 = 85.9
w2 = 1164.1

# --- Cálculo da Curva Real Exata ---
numerator = [100000]
denominator = [1, 1250, 100000]
transfer_function = signal.TransferFunction(numerator, denominator)
w_exact, mag_exact, phase_exact = signal.bode(transfer_function, w)

# --- Cálculo de Todas as Assíntotas ---

# 1. Assíntota G1 (Numerador)
g1_asymptote = np.full_like(w, 100)

# 2. Assíntota G2 (Pólo em w1)
g2_val_flat = -20 * np.log10(w1)
g2_asymptote = np.piecewise(w,
    [w < w1, w >= w1],
    [g2_val_flat, lambda w: g2_val_flat - 20 * (np.log10(w) - np.log10(w1))]
)

# 3. Assíntota G3 (Pólo em w2)
g3_val_flat = -20 * np.log10(w2)
g3_asymptote = np.piecewise(w,
    [w < w2, w >= w2],
    [g3_val_flat, lambda w: g3_val_flat - 20 * (np.log10(w) - np.log10(w2))]
)

# 4. Assíntota Resultante (Soma das outras três)
final_asymptote = g1_asymptote + g2_asymptote + g3_asymptote

# --- Plotando o Gráfico de Bode (Magnitude e Fase) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# --- Plot de Magnitude ---
ax1.semilogx(w, g1_asymptote, 'r:', label='G1: Assíntota Numerador')
ax1.semilogx(w, g2_asymptote, 'g:', label='G2: Assíntota Pólo 1')
ax1.semilogx(w, g3_asymptote, 'purple', linestyle=':', label='G3: Assíntota Pólo 2')
ax1.semilogx(w, final_asymptote, 'k--', linewidth=2, label='Assíntota Resultante')
ax1.semilogx(w_exact, mag_exact, 'b', linewidth=2.5, label='Curva Real Exata')

ax1.set_title('Diagrama de Bode - Magnitude e Fase', fontsize=16)
ax1.set_ylabel('Magnitude (dB)')
ax1.set_ylim(-80, 120)
ax1.grid(which='both', linestyle='--')
ax1.legend()

# --- Plot de Fase ---
ax2.semilogx(w_exact, phase_exact, 'b', linewidth=2.5, label='Fase Real Exata')
ax2.set_ylabel('Fase (graus)')
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylim(-180, 0)
ax2.grid(which='both', linestyle='--')
ax2.legend()

plt.tight_layout()
plt.show()
