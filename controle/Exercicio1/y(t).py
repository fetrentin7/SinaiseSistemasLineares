import matplotlib.pyplot as plt
import numpy as np

# --- Definição do Tempo ---
# Cria um vetor de tempo de 0 a 1.5 segundos, com 500 pontos para um gráfico suave.
# A resposta é rápida (devido a e^-8t), então 1.5s é mais que suficiente.
t = np.linspace(0, 1.5, 500)

# --- Cálculo da Função de Saída y(t) ---
# Aplica a fórmula que encontramos para cada ponto no tempo.
y = 0.5 * (1 - np.exp(-8 * t))

# --- Criação do Gráfico ---
# Cria uma figura para o plot
plt.figure(figsize=(10, 6))

# Plota o tempo no eixo x e y(t) no eixo y
plt.plot(t, y, label='Resposta y(t)', linewidth=2)

# --- Configurações Visuais do Gráfico ---
# Adiciona um título
plt.title('Resposta ao Degrau do Sistema em Malha Aberta', fontsize=16)

# Adiciona rótulos aos eixos
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Amplitude de Saída y(t)', fontsize=12)

# Adiciona uma grade
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona uma linha pontilhada para mostrar o valor final de estabilização
plt.axhline(y=0.5, color='red', linestyle='--', label='Valor Final = 0.5')

# Adiciona a legenda para identificar as linhas
plt.legend()

# --- Exibição do Gráfico ---
plt.show()
