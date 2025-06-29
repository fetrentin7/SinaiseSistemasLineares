import matplotlib.pyplot as plt
import numpy as np

# --- Definição dos Parâmetros ---
# Valores de K para analisar
k_values = [1, 2, 10, 100]
# Cores para cada par de pólos no gráfico, para facilitar a distinção
colors = ['red', 'green', 'blue', 'purple']

# --- Criação do Gráfico ---
fig, ax = plt.subplots(figsize=(8, 8))

# --- Loop para Calcular e Plotar cada Par de Pólos ---
# O 'zip' junta as duas listas (k_values e colors) para usá-las ao mesmo tempo.
for k, color in zip(k_values, colors):
    # Calcula a parte imaginária do pólo para o K atual, usando a fórmula que deduzimos.
    imag_part = 10 * np.sqrt(k)

    # Define os dois pólos complexos conjugados: s = -10 + j*imag_part e s = -10 - j*imag_part
    poles = [-10 + 1j * imag_part, -10 - 1j * imag_part]

    # Plota os pólos no gráfico. A função np.real() pega a parte real (-10)
    # e np.imag() pega a parte imaginária (+ ou - imag_part).
    ax.scatter(np.real(poles), np.imag(poles), s=150, marker='x', color=color, linewidth=2, label=f'Pólos para K = {k}')

# --- Configurações Visuais do Gráfico ---
ax.set_title('Diagrama de Pólos para Malha Fechada (Exercício 2)', fontsize=16)
ax.set_xlabel('Eixo Real (σ)', fontsize=12)
ax.set_ylabel('Eixo Imaginário (jω)', fontsize=12)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend()
ax.axis('equal')  # Garante que a escala dos eixos seja a mesma, para não distorcer a geometria

# --- Exibição do Gráfico ---
plt.show()
