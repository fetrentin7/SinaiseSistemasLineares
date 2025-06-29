import matplotlib.pyplot as plt
import numpy as np

# --- Definição do Tempo e dos Ganhos K ---
t = np.linspace(0, 2.5, 1000)  # Tempo maior para ver as oscilações
k_values = [1, 2, 10, 100]

# --- Criação do Gráfico ---
plt.figure(figsize=(12, 8))

# --- Loop para Calcular e Plotar cada Resposta ---
for k in k_values:
    # Coeficiente A (valor final)
    A = k / (1 + k)

    # Frequência de oscilação omega
    omega = 10 * np.sqrt(k)

    # Fator do seno (alpha/omega)
    sin_factor = 1 / np.sqrt(k)

    # Calcula a resposta y(t) usando a fórmula completa
    y = A * (1 - np.exp(-10 * t) * (np.cos(omega * t) + sin_factor * np.sin(omega * t)))

    # Plota a resposta y(t)
    plt.plot(t, y, label=f'Resposta para K = {k}', linewidth=2)

# --- Configurações Visuais do Gráfico ---
plt.title('Respostas ao Degrau em Malha Fechada (Exercício 2)', fontsize=16)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Amplitude de Saída y(t)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.axhline(y=1, color='black', linestyle=':', label='Alvo (Entrada Degrau) = 1')
plt.legend()
plt.ylim(0, 1.6)  # Aumentamos o eixo Y para ver o overshoot

# --- Exibição do Gráfico ---
plt.show()
