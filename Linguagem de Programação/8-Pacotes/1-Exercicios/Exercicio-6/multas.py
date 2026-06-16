def calcular_infracao(limite_via, velocidade_carro):
    if velocidade_carro <= limite_via:
        print("Boa viagem! Dentro do limite.")
    elif velocidade_carro > limite_via and velocidade_carro <= limite_via + 20:
        print("Infração Média! Multa de R$ 130,16.")
    elif velocidade_carro > limite_via +20:
        print("Infração Gravíssima! Multa de R$ 880,41 e suspensão da CNH.")