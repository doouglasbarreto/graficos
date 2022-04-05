import matplotlib.pyplot as plt
import numpy as np

class Dados:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

vetorDeObjetos = []
contador = 1
while (contador < 5):
    entradaNome = input('Digite o nome do ' + str(contador) + 'º item: ')
    entradaValor = input('Digite o valor do ' + str(contador) + 'º item: ')
    vetorDeObjetos.append(Dados(entradaNome, entradaValor))
    contador += 1

# Valores do Gráfico #
y = np.array([vetorDeObjetos[0].valor, vetorDeObjetos[1].valor, vetorDeObjetos[2].valor, vetorDeObjetos[3].valor])

# Itens do Gráfico #
mylabels = [vetorDeObjetos[0].nome, vetorDeObjetos[1].nome, vetorDeObjetos[2].nome, vetorDeObjetos[3].nome]


# Espaço entre as 'fatias' do gráfico #
myexplode = [0.2, 0, 0, 0]

# Monta o gráfico e depois o mostra na tela #
plt.pie(y, labels=mylabels, explode=myexplode, shadow=True)
plt.show()