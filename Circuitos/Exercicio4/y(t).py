# Importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Definição do Sistema ---

# Valores dos componentes do circuito
R = 10.0  # Ohms
L = 0.1   # Henry
C = 10e-6 # 10 microFarads (10 * 10^-6 F)

# Coeficientes da função de transferência H(s)
# H(s) = (s^2 + 1/LC) / (s^2 + (R/L)s + 1/LC)
# calcular os coeficientes a partir dos componentes para garantir a precisão.
R_L = R / L               # 10 / 0.1 = 100
one_over_LC = 1 / (L * C) # 1 / (0.1 * 10e-6) = 1,000,000

# Numerador da H(s): [1*s^2, 0*s, 1/LC]
num = [1, 0, one_over_LC]
# Denominador da H(s): [1*s^2, (R/L)*s, 1/LC]
den = [1, R_L, one_over_LC]

# Criar o objeto do sistema LTI (Linear Time-Invariant) que representa H(s)
system = signal.TransferFunction(num, den)

# --- Simulação e Cálculo ---

# 1. Simulação da resposta ao degrau pela biblioteca
# Define um vetor de tempo para a simulação para garantir boa resolução do gráfico.
# O sistema se estabiliza em cerca de 0.1s, então plotamos até 0.15s.
t_sim = np.linspace(0, 0.15, 2000)

# A função 'step' calcula a resposta para um degrau de amplitude 1.
t_sim, y_sim_unit = signal.step(system, T=t_sim)

# A entrada real era um degrau de 2, então multiplicamos a saída por 2.
y_sim = 2 * y_sim_unit

# 2. Cálculo da nossa solução analítica
# vo(t) = 2 - 0.2 * e^(-50t) * sin(998.75t)
# Os valores 50 e 998.75 vêm dos polos p = -50 ± j998.75
alpha = 50      # Termo de decaimento exponencial
omega = 998.75  # Frequência angular da oscilação
y_analytical = 2 - 0.2 * np.exp(-alpha * t_sim) * np.sin(omega * t_sim)

# --- Geração do Gráfico ---

# Cria a figura e os eixos para o gráfico
plt.figure(figsize=(12, 7))


# Plota a resposta simulada (linha azul, grossa)
plt.plot(t_sim, y_sim, 'b-', linewidth=4, label='Resposta Simulada (da biblioteca SciPy)')

# Plota a resposta analítica (linha vermelha, tracejada) para confirmar
plt.plot(t_sim, y_analytical, 'r--', linewidth=2, label='Solução Analítica (Fórmula)')

# ADICIONA A LINHA DE REFERÊNCIA HORIZONTAL EM 2V
# Em preto e pontilhada, com zorder=0 para ficar no fundo
plt.axhline(y=2, color='k', linestyle=':', linewidth=2, label='Valor Final (2V)', zorder=0)

# Adiciona títulos, legendas e grade para clareza
plt.title('Gráfico Final: Resposta Completa do Sistema', fontsize=16)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Tensão de Saída Vo(t) (V)', fontsize=12)
plt.grid(True)
plt.legend(fontsize=12)

# Mostra o gráfico final
plt.show()
