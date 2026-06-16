'''
1. Crie um arquivo chamado multas.py. Lá dentro, crie uma função 
chamada calcular_infracao(limite_via, velocidade_carro).

2. A função deve calcular se o carro ultrapassou o limite e aplicar 
a seguinte regra:

    * Se a velocidade do carro for menor ou igual ao limite da via: 
    Retornar "Boa viagem! Dentro do limite."

    * Se a velocidade ultrapassar o limite em até 20 km/h (inclusive):
    Retornar "Infração Média! Multa de R$ 130,16."

    * Se ultrapassar o limite em mais de 20 km/h: 
    Retornar "Infração Gravíssima! Multa de R$ 880,41 e suspensão da CNH."

3. Crie o arquivo main.py. Importe a função. Solicite ao usuário que 
digite qual é o limite da avenida e, em seguida, qual foi a 
velocidade registrada. Envie os dois valores para a função e mostre 
o resultado final.
'''

import multas

limite = int(input("Digite o limite da via: "))
velocidade = int(input("Digite a velocidade do carro: "))

multas.calcular_infracao(limite, velocidade)
