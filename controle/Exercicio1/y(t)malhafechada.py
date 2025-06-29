import matplotlib.pyplot as plt
import numpy as np

# --- Definição do Tempo e dos Ganhos K ---
# A resposta mais lenta é para K=1 (polo em -12). 5*(1/12) ~ 0.4s.
# Usaremos um tempo de 0 a 0.5 segundos para ver todas as respostas se estabilizando.
t = np.linspace(0, 0.5, 500)
k_values = [1, 10, 20]

# --- Criação do Gráfico ---
plt.figure(figsize=(10, 6))

# --- Loop para Calcular e Plotar cada Resposta ---
for k in k_values:
    # Coeficiente A (valor final) para o K atual
    A = (4 * k) / (8 + (4 * k))

    # Expoente da exponencial para o K atual
    exponent_factor = -(8 + (4 * k))

    # Calcula a resposta y(t)
    y = A * (1 - np.exp(exponent_factor * t))

    # Plota a resposta y(t)
    plt.plot(t, y, label=f'Resposta para K = {k}', linewidth=2)

    # Plota a linha do valor final para referência
    plt.axhline(y=A, linestyle='--', alpha=0.7, label=f'Valor Final (K={k}) = {A:.2f}')

# --- Configurações Visuais do Gráfico ---
plt.title('Respostas ao Degrau em Malha Fechada para Diferentes Ganhos K', fontsize=16)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Amplitude de Saída y(t)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.ylim(0, 1.1)  # Ajusta o limite do eixo Y para melhor visualização

# --- Exibição do Gráfico ---
plt.show()