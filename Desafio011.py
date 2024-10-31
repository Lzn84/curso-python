    #calculo para descobrir a area da parede 
altura = float(input('digite a altura da sua parede:'))
largura = float(input('Digite a largura da sua parede:'))
area = altura * largura
    #descobrindos os baldes de tintas necessários
tinta = 2 
valor = area / tinta
print(f'O total de baldes de tintas necessários será:{valor}.')

