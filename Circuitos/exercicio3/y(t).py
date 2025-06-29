import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Definir os valores dos componentes
L = 0.1  # H
C = 100e-6  # F (100uF)
R = 8  # Ohms

# Coeficientes da função de transferência H(s)
# H(s) = (1/LC) / (s^2 + (1/RC)*s + 1/LC)
num = [1 / (L * C)]
den = [1, 1 / (R * C), 1 / (L * C)]

# Criar o objeto da Função de Transferência
# A biblioteca scipy.signal é a ferramenta padrão para isso
system = signal.TransferFunction(num, den)



# Calcular a resposta ao degrau unitário (amplitude 1)
# A função retorna o vetor de tempo (t) e o vetor de saída (yout)
t, yout = signal.step(system)

# Ajustar a saída para a amplitude do degrau correta (2V)
yout_final = yout * 2

# --- Plotar o gráfico ---
plt.figure(figsize=(10, 6))
plt.plot(t, yout_final, label='Tensão de Saída y(t) (simulada)', color='blue', linewidth=2)
plt.axhline(y=2, color='r', linestyle='--', label=f'Valor Final ()')
plt.title('Resposta do Circuito a um Degrau de 2u(t)')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão de Saída (V)')
plt.grid(True)
plt.legend()
plt.show()

