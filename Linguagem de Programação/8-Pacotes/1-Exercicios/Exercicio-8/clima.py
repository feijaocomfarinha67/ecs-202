def avaliar_temp(graus):
    if graus < 20:
        return "Frio"
    elif graus >= 20 and graus <= 28:
        return "Agradável"
    else:
        return "Calor"
