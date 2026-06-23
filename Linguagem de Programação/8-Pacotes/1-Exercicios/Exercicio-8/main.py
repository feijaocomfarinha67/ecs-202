'''
Exercício 8: A Estação Meteorológica de Itajaí (Nível: Intermédio/Avançado)

Objetivo: Utilizar um laço for com a função range() para recolher um número fixo e predeterminado de dados, 
enviando-os a cada iteração para avaliação num módulo externo.


1. Cria um ficheiro chamado clima.py. Lá dentro, desenvolve uma função chamada avaliar_temp(graus).

2. A regra de negócio é a seguinte:

    * Se graus for menor do que 20, a função devolve "Frio".

    * Se for entre 20 e 28 (inclusive), devolve "Agradável".

    * Se for maior do que 28, devolve "Calor".

3. Cria o ficheiro main.py e importa a função avaliar_temp.

4. No programa principal, cria um laço for que se repita exatamente 5 vezes 
(simulando os dias úteis da semana). 

Dica: usa range(1, 6).

5. Em cada volta do laço, pede ao utilizador para digitar a temperatura prevista para esse dia (guarda na variável temp).

6. Chama a função, passando a variável temp como parâmetro, e guarda a resposta numa variável chamada estado. 
Exibe o resultado no terminal.
'''