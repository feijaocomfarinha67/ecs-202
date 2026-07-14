'''
O Caixa do Ferry Boat (Nível: Intermédio/Avançado)
Objetivo: Criar um programa que funcione de forma contínua usando o laço while, onde o utilizador escolhe opções numéricas num "menu". O módulo fará a conversão da opção para o valor financeiro correspondente, e o programa principal acumulará o dinheiro no caixa.

Enunciado:

Cria um ficheiro chamado ferry.py. Lá dentro, desenvolve uma função chamada tarifa(tipo).

A regra de cobrança da travessia é:

Se o tipo for 1 (Bicicleta), devolve 2 (reais).

Se for 2 (Moto), devolve 5.

Se for 3 (Carro), devolve 10.

Se for digitado qualquer outro número, devolve 0.

Cria o ficheiro main.py e importa a função tarifa.

No programa principal, cria uma variável caixa = 0 (para guardar o total do turno).

Cria uma variável op = -1 (para iniciar o laço).

Cria um laço while que continue a executar enquanto a op (opção) for diferente de 0.

Dentro do laço, pede ao utilizador para digitar a opção (1, 2, 3 ou 0 para encerrar).

Envia a op para a função, guarda o resultado na variável valor e soma ao caixa.

Fora do laço, imprime o total arrecadado pelo operador do ferry boat.
'''