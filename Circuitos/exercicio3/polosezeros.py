import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Função de Transferência---
# Numerador: s^2 + 0*s + 1,000,000
numerador = [1, 0, 1_000_000] # Use underscores for readability in large numbers

# Denominador: s^2 + 100*s + 1,000,000
denominador = [1, 100, 1_000_000] # Use underscores for readability in large numbers


# 2. Cria o objeto do sistema e extrai os polos e zeros
sistema = signal.TransferFunction(numerador, denominador)
polos = sistema.poles
zeros = sistema.zeros

# Imprime os valores no console para verificação
print(f"Analisando H(s) = {sistema}")
print("---------------------------------")
print(f"Polos do sistema: {np.round(polos, 4)}") # Arredondando para melhor leitura
print(f"Zeros do sistema: {np.round(zeros, 4)}") # Arredondando para melhor leitura


# --- 3. Criação do Gráfico de Polos e Zeros ---
plt.figure(figsize=(8, 8))

# Plota os polos com 'x' vermelhos
plt.scatter(np.real(polos), np.imag(polos), s=150, marker='x', color='red', label='Polos')

# Plota os zeros com 'o' azuis (apenas se existirem)
if len(zeros) > 0:
    plt.scatter(np.real(zeros), np.imag(zeros), s=150, marker='o',
                facecolors='none', edgecolors='blue', linewidths=1.5, label='Zeros')

# Configurações para deixar o gráfico mais claro
plt.axhline(0, color='black', lw=1) # Eixo horizontal
plt.axvline(0, color='black', lw=1) # Eixo vertical
plt.grid(True, linestyle='--', alpha=0.6)

# Adiciona os títulos, legendas e nomes dos eixos
plt.title('Diagrama de Polos e Zeros', fontsize=16)
plt.xlabel(r'Eixo Real ($\sigma$)', fontsize=12)
plt.ylabel(r'Eixo Imaginário ($j\omega$)', fontsize=12)
plt.legend(fontsize=12)

# Set limits to better visualize the plot
# You might need to adjust these based on the exact pole/zero values
max_val = max(abs(p) for p in list(polos) + list(zeros)) * 1.1 # 10% buffer
plt.xlim(-max_val, max_val)
plt.ylim(-max_val, max_val)

plt.axis('equal') # Ensures that the scale on the real and imaginary axes is the same

plt.show()