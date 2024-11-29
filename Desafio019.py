# Armazenando nomes
import random
nomes = []
quantidade = int(input('Escolha a quantidade que deseja sortear: '))
# Recebendo nomes
for i in range(quantidade):nome = input(f'Dgite o nome {i +  1}: ')
nomes.append(nome)
# Sorteando
sorteado = random.choice(nomes)
print(f'O nome sorteado foi: {sorteado}')
