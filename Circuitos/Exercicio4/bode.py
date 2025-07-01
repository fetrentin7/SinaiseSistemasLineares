import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# --- 1. Definição da Função de Transferência ---
# H(s) = (s^2 + 1.000.000) / (s^2 + 100s + 1.000.000)
num = [1, 0, 1000000]
den = [1, 100, 1000000]
sistema = sig.TransferFunction(num, den)

# Frequência de corte (natural) e do notch
w_c = 1000

# --- 2. Cálculo da Resposta em Frequência ---
# Gera um range de frequências em escala logarítmica
# Aumentamos os pontos para capturar bem o "notch"
frequencias = np.logspace(1, 5, 10000)
w, mag, phase = sig.bode(sistema, frequencias)

# --- 3. Plotagem do Diagrama de Bode ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True) # sharex para alinhar os eixos x

# --- Gráfico de Magnitude ---
ax1.semilogx(w, mag, color='blue', label='Curva Real', zorder=5)
ax1.set_title('Diagrama de Bode: Magnitude', fontsize=16)
ax1.set_ylabel('Magnitude (dB)')
ax1.grid(True, which='both')
ax1.set_ylim(-80, 5) # Ajusta o limite de y para ver o notch e as assíntotas

# --- Plotando as Assíntotas de Magnitude ---
# A assíntota é 0 dB, mas com uma indicação do notch infinito.
ax1.plot(w, np.zeros_like(w), 'r--', label='Assíntota (0 dB)', zorder=4)
# Desenhamos uma linha vertical para representar o notch ideal (-inf dB)
ax1.plot([w_c, w_c], [0, -80], 'r--', zorder=4)
ax1.legend()


# --- Gráfico de Fase ---
ax2.semilogx(w, phase, color='green', label='Curva de Fase', zorder=5)
ax2.set_title('Diagrama de Bode: Fase', fontsize=16)
ax2.set_xlabel('Frequência (rad/s)')
ax2.set_ylabel('Fase (graus)')
ax2.grid(True, which='both')
ax2.set_yticks(np.arange(0, -100, -15)) # Melhora a visualização dos graus

# --- Plotando a Assíntota de Fase (Aproximação em "V") ---
# Pontos da assíntota: (início, vale, fim)
# O "vale" ocorre em w_c. O início e fim podem ser uma década antes/depois,
# ou ajustados para melhor visualização. Vamos usar 500 rad/s e 2000 rad/s.
w_asym_phase = [500, w_c, 2000]
phase_asym = [0, -90, 0]
ax2.plot(w_asym_phase, phase_asym, 'm:', label='Assíntota Aproximada', zorder=4)
ax2.legend()

# Marca a frequência do notch em ambos os gráficos
ax1.axvline(w_c, color='g', linestyle=':', label=f'ω = {w_c} rad/s', zorder=3)
ax2.axvline(w_c, color='g', linestyle=':', zorder=3)


plt.tight_layout() # Ajusta o espaçamento entre os gráficos
plt.show()