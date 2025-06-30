import matplotlib.pyplot as plt
import numpy as np

# --- Definição dos Pólos e Zeros ---
# Estes são os valores que calculamos para Y(s) = 4 / (s*(s+8))
poles = [0, -8]
zeros = [] # Lista vazia porque não há zeros

# --- Criação do Gráfico ---
# Cria uma figura e um conjunto de eixos para o plot
fig, ax = plt.subplots(figsize=(8, 6))

# --- Plotando os Pontos ---
# Plota os pólos como marcadores 'x' vermelhos
ax.scatter(np.real(poles), np.imag(poles), s=150, marker='x', color='red', linewidth=2, label='Pólos')

# Se a lista de zeros não estiver vazia, plota os zeros como 'o' azuis
if zeros:
    ax.scatter(np.real(zeros), np.imag(zeros), s=150, marker='o', facecolors='none', edgecolors='blue', linewidth=2, label='Zeros')

# --- Configurações Visuais do Gráfico ---
ax.set_title('Diagrama de Pólos e Zeros para Y(s)', fontsize=16)

# Adiciona rótulos aos eixos x (Real) e y (Imaginário)
ax.set_xlabel('Eixo Real (σ)', fontsize=12)
ax.set_ylabel('Eixo Imaginário (jω)', fontsize=12)

# Desenha as linhas dos eixos horizontal e vertical para uma melhor visualização
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)

# Adiciona uma grade ao fundo
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Força a escala dos eixos a ser a mesma para evitar distorções
ax.axis('equal')

# Adiciona a legenda
ax.legend()

# --- Anotações (Opcional, mas útil) ---
# Adiciona texto para identificar cada pólo
for pole in poles:
    ax.text(np.real(pole) + 0.2, np.imag(pole) + 0.2, f's = {pole}', va='bottom', ha='left')

# --- Exibição do Gráfico ---
# Mostra o gráfico final
plt.show()