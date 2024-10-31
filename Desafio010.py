taxa_cambio = 0.18 
def converter_reais_para_dolares(valor_em_reais):
valor_em_dolares = valor_em_reais * taxa_cambio
return valor_em_dolares

valor_reais = float(
    input("Digite o valor em reais (BRL) que deseja converter para dólares (USD): "))
valor_dolares = converter_reais_para_dolares(valor_reais)
print(f"R$ {valor_reais} equivale a aproximadamenge $ {valor_dolares:.2f} USD")
