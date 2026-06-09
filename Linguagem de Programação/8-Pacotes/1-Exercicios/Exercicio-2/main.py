'''
1. Crie um arquivo chamado conversores.py. Dentro dele, crie uma 
função pes_para_metros(pes) que receba uma medida em pés e retorne o 
valor convertido para metros (multiplique os pés por 0.3048).

2. No arquivo main.py, importe apenas a função pes_para_metros. 
Peça para o usuário digitar a altura de um container em pés, chame a 
função e exiba o resultado em metros (sem usar o prefixo do módulo).
'''
from conversores import pes_para_metros

pes = float(input("Digite uma altura em pés: "))

metros = pes_para_metros(pes)

# usando f-strings com duas casas decimais
print(f"A altura informada é: {metros:.2f}m")


