'''
Crie um arquivo chamado seguranca.py. Dentro dele, crie uma função 
chamada validar_login(nome, senha). Se o nome digitado for igual 
a "admin", e a senha for igual a “123Testar” a função deve retornar 
a frase: "Acesso Liberado!". Caso contrário, deve retornar: "Acesso 
negado!".

Crie um segundo arquivo chamado main.py na mesma pasta. Importe a 
função validar_usuario. No programa principal, use um input para 
perguntar o nome do usuário, passe esse nome para a função importada 
e exiba a resposta na tela.
'''

def valida_login(nome, senha):
    if nome == "Admin" and senha == "123Testar":
        print("Acesso liberado!")
    else:
        print("Acesso negado!")