'''
Enunciado para a Turma:
Crie um arquivo chamado jogo_adivinhacao.py.
Importe o módulo nativo random na primeira linha.
Use a função random.randint(1, 50) para fazer o computador "pensar" em um número aleatório entre 1 e 50. Guarde isso na variável secreto.
Crie uma variável palpite = 0 (para iniciar o laço) e uma variável tentativas = 0 (para contar quantas vezes o jogador jogou).
Crie um laço while que continue rodando enquanto o palpite for diferente do secreto.
Dentro do laço, peça o palpite do usuário, some 1 às tentativas e use a estrutura if/elif/else para dar dicas:
Se o palpite for menor que o segredo: imprima "Tente um número MAIOR!"
Se o palpite for maior que o segredo: imprima "Tente um número MENOR!"
Se acertar: imprima uma mensagem de parabéns mostrando o número de tentativas.
'''

import random

secreta = random.randint(1, 50)
palpite = 0 
tentativas = 0

while palpite != secreta:
    palpite = int(input("Digite um número: "))
    tentativas += 1

    if palpite < secreta:
        print("Digite um número MAIOR!")
    elif palpite > secreta:
        print("Digite um número MENOR")
    else:
        print("Parabéns você acertou", secreta)
        print("Você usou: ", tentativas)