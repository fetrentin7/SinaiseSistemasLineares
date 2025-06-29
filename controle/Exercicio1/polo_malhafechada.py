import matplotlib.pyplot as plt
import numpy as np

# Valores de K para analisar
k_values = [1, 10, 20]
# Cores para cada valor de K no gráfico
colors = ['red', 'green', 'blue']

# Cria a figura e os eixos
fig, ax = plt.subplots(figsize=(10, 6))

# Loop para calcular e plotar o pólo para cada K
for k, color in zip(k_values, colors):
    # Calcula a posição do pólo para o K atual
    pole = -(8 + 4 * k)

    # Plota o pólo no gráfico
    ax.scatter(np.real(pole), np.imag(pole), s=150, marker='x', color=color, linewidth=2, label=f'Pólo para K = {k}')

    # Adiciona uma anotação de texto
    ax.text(np.real(pole) + 1, np.imag(pole) + 0.05, f's = {pole}', va='bottom', ha='left', color=color)

# Configurações visuais do gráfico
ax.set_title('Diagrama de Pólos para Malha Fechada com Variação de K', fontsize=16)
ax.set_xlabel('Eixo Real (σ)', fontsize=12)
ax.set_ylabel('Eixo Imaginário (jω)', fontsize=12)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend()

# Exibe o gráfico
plt.show()