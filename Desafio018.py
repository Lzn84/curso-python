# Montando a formula
import math
a = float(input('Escolha um ângulo em graus:'))
ar = math.radians(a)
# Calculando seno, cosseno e tangente
seno = math.sin(ar)
cosseno = math.cos(ar)
tangente = math.tan(ar)
# Exbição
print(f'Seno de {a} = {seno:.2}.\nCosseno de {a} = {
      cosseno:.2}.\nTangente de {a} = {tangente:.2}.')
