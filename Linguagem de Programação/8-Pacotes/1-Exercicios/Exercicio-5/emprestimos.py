def verificar_atraso(dias):
    if dias > 0:
        print("Empréstimo bloqueado! Devolva o equipamento pendente.")
    elif dias == 0:
        print("Empréstimo liberado! Pode retirar novo equipamento.")
