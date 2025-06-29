import matplotlib.pyplot as plt
import numpy as np

# --- Definição do Tempo ---
# Os pólos estão em -10, então a resposta é rápida.
# Um tempo de 0 a 1 segundo é suficiente para ver tudo.
t = np.linspace(0, 1, 500)

# --- Cálculo da Função de Saída y(t) ---
# Aplica a fórmula que encontramos para o sistema com pólo duplo.
y = 1 - np.exp(-10 * t) * (1 + 10 * t)

# --- Criação do Gráfico ---
plt.figure(figsize=(10, 6))

# Plota o tempo no eixo x e y(t) no eixo y
plt.plot(t, y, label='Resposta y(t) (Criticamente Amortecida)', linewidth=2, color='green')

# --- Configurações Visuais do Gráfico ---
plt.title('Resposta ao Degrau do Sistema do Exercício 2 (Malha Aberta)', fontsize=16)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Amplitude de Saída y(t)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona uma linha pontilhada para mostrar o valor final de estabilização
plt.axhline(y=1, color='red', linestyle='--', label='Valor Final = 1')

# Adiciona a legenda para identificar as linhas
plt.legend()
plt.ylim(0, 1.1)

# --- Exibição do Gráfico ---
plt.show()