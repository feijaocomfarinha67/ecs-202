'''
Crie um script único chamado inspecionar_math.py. 
Importe o módulo nativo de matemática do Python (import math). 
Utilize a função dir() para listar tudo o que existe dentro 
dele e imprima essa lista no terminal. 
Escolha uma função que apareceu na lista (como sqrt 
para raiz quadrada ou pow para potência) e tente aplicar no 
código.
'''

import math

# recursos = dir(math)
# print(recursos)

base = int(input("Digite  o número base: "))
expoente = int(input("Digite a quandidade de vezes que a base será multiplicada: "))

print("O resultado é: ", math.pow(base, expoente))
