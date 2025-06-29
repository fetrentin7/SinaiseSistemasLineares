import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# --- Função de Transferência---
numerador = [50,50e3]
denominador = [1, 550, 50e3]

sistema = signal.TransferFunction(numerador, denominador)

# --- 2. Cálculo da Resposta ao Degrau ---
# A função signal.step calcula a resposta para um degrau unitário u(t).
t, y_unitario = signal.step(sistema)

# Como a entrada é 2u(t) e o sistema é linear, multiplicamos a saída por 2.
y_final = 2 * y_unitario

# --- 3. Criação do Gráfico ---
plt.figure(figsize=(10, 6))

# Plota a entrada x(t) = 2u(t) para comparação
plt.plot(t, 2 * np.ones_like(t), 'r--', linewidth=2, label='Entrada x(t) = 2u(t)')

# Plota a saída y(t)
plt.plot(t, y_final, 'b-', linewidth=2, label='Saída y(t)')

# Configurações do gráfico
# Título corrigido para a função atual
plt.title('Resposta ao Degrau do Filtro Passa-Faixa', fontsize=14)
plt.xlabel('Tempo (s)', fontsize=12)
plt.ylabel('Tensão (V)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--')

# Mostra o gráfico
plt.show()