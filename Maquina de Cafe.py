def MaqCafe(a1, a2, a3):

    andares = ["terreo"]
    andares.append(a1), andares.append(a2), andares.append(a3)

    tempo_por_andar = [None]
    menor = 6001
    aux = ""

    tempo_por_andar.append(andares[2]*2 + andares[3]*4), tempo_por_andar.append(andares[1]*2 + andares[3]*2), tempo_por_andar.append(andares[1]*4 + andares[2]*2)

    for andar in range(1, len(tempo_por_andar)):
        if menor == tempo_por_andar[andar]:
            aux += " ou {andar}º andar".format(andar = andar)

        if menor > tempo_por_andar[andar]:
            menor = tempo_por_andar[andar]

    return "O melhor andar para colocar a máquina é {andar}º andar{empate}, gastando o tempo diário de {tempo} minutos.".format(andar = tempo_por_andar.index(menor),empate = aux, tempo = menor)

a1 = int(input("Digite o número de trabalhadores no 1º andar: "))
a2 = int(input("Digite o número de trabalhadores no 2º andar: "))
a3 = int(input("Digite o número de trabalhadores no 3º andar: "))
print(MaqCafe(a1,a2,a3))