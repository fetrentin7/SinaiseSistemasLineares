import matplotlib.pyplot as plt
import numpy as np

# --- Definição dos Pólos e Zeros (Exercício 2) ---
# Usamos uma lista simples, como no seu código original.
# Para o polo duplo, simplesmente o colocamos duas vezes na lista.
poles = [0, -10, -10]
zeros = []

# --- Criação do Gráfico ---
fig, ax = plt.subplots(figsize=(8, 6))

# --- Plotando os Pontos ---
# Esta linha não muda. Ela vai desenhar um 'X' na origem e dois 'X' sobrepostos em -10.
ax.scatter(np.real(poles), np.imag(poles), s=150, marker='x', color='red', linewidth=2, label='Pólos')

if zeros:
    ax.scatter(np.real(zeros), np.imag(zeros), s=150, marker='o', facecolors='none', edgecolors='blue', linewidth=2,
               label='Zeros')

# --- Configurações Visuais do Gráfico (Não muda nada aqui) ---
ax.set_title('Diagrama de Pólos e Zeros para Y(s) do Exercício 2', fontsize=16)
ax.set_xlabel('Eixo Real (σ)', fontsize=12)
ax.set_ylabel('Eixo Imaginário (jω)', fontsize=12)
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.axis('equal')
ax.legend()

# --- Anotações (AQUI ESTÁ A ADAPTAÇÃO) ---
# Para evitar escrever o texto duas vezes no mesmo lugar, primeiro pegamos os pólos únicos.
unique_poles = sorted(list(set(poles)))  # Isso resulta em [0, -10]

# Agora, para cada pólo único, contamos quantas vezes ele aparece na lista original.
for pole in unique_poles:
    multiplicity = poles.count(pole)  # Conta as ocorrências

    # Se a multiplicidade for maior que 1, escrevemos o texto com a contagem.
    if multiplicity > 1:
        ax.text(np.real(pole) + 0.3, np.imag(pole) + 0.3, f'({multiplicity}) s = {pole}', va='bottom', ha='left')
    # Caso contrário, escrevemos o texto normalmente.
    else:
        ax.text(np.real(pole) + 0.3, np.imag(pole) + 0.3, f's = {pole}', va='bottom', ha='left')

# --- Exibição do Gráfico ---
plt.show()