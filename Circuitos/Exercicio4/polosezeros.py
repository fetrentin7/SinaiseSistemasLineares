import numpy as np
import matplotlib.pyplot as plt

# --- 1. Definição da Função de Transferência ---
# H(s) = 100.000 / (s^2 + 1250s + 100.000)

# Coeficientes do polinômio do numerador (em ordem decrescente de potência de s)
numerador = [1,0, 1000000]

# Coeficientes do polinômio do denominador
denominador = [1, 100, 1000000]


# --- 2. Cálculo dos Polos e Zeros ---
# A função np.roots() encontra as raízes de um polinômio a partir de seus coeficientes
polos = np.roots(denominador)
zeros = np.roots(numerador)

# Imprime os valores no console para verificação
print(f"Polos encontrados: {polos}")
print(f"Zeros encontrados: {zeros}")


# --- 3. Criação do Gráfico (Plano-s) ---
plt.figure(figsize=(10, 7))

# Adiciona linhas para os eixos real e imaginário
plt.axhline(y=0, color='k', linestyle='--', linewidth=0.8)
plt.axvline(x=0, color='k', linestyle='--', linewidth=0.8)

# Plota os polos no gráfico usando 'x' como marcador
plt.scatter(np.real(polos), np.imag(polos), s=150, marker='x', color='red', label='Polos')

# Plota os zeros (se existirem) usando 'o' como marcador
if zeros.size > 0:
    plt.scatter(np.real(zeros), np.imag(zeros), s=150, marker='o',
                edgecolor='blue', facecolor='none', linewidths=1.5, label='Zeros')

# --- 4. Configuração e Exibição do Gráfico ---
plt.title('Diagrama de Polos e Zeros', fontsize=16)
plt.xlabel('Eixo Real ($\sigma$)', fontsize=12)
plt.ylabel('Eixo Imaginário ($j\omega$)', fontsize=12)
plt.grid(True, which='both', linestyle=':', linewidth=0.5)
plt.legend(fontsize=12)

# Ajusta os limites dos eixos para uma melhor visualização
plt.xlim(-1300, 100)

# Garante que os eixos tenham uma escala visualmente adequada
plt.gca().set_aspect('auto') # 'auto' para se ajustar melhor a polos distantes

# Exibe o gráfico
plt.show()