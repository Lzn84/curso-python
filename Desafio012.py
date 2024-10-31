# calcúlo do produto
item = float(
    input('Digite o valor do item que você quer receber 5% de desconto:'))
n5 = item * (5 / 100)
desconto = item - n5
# Valor na tela
print(f'Seu novo preço com desconto é: {desconto}$')
