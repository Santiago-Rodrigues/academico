# Pedro Abrantes Condé
# Santiago da Silva Rodrigues

jogo = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]


def inserir_jogada(jogo):
    pos1 = int(input("Digite a linha: "))
    pos2 = int(input("Digite a coluna: "))
    while 1 < pos1 > 3 or 1 < pos2 > 3:
        print("Jogada inválida")
        pos1 = int(input("Digite a linha: "))
        pos2 = int(input("Digite a coluna: "))
    jogada = jogo[pos1 - 1][pos2 - 1]
    return jogada


def substituir_por_x(jogo):
    jogou = False
    while jogou == False:
        print("Jogador X")
        jogada = inserir_jogada(jogo)
        for i in range(len(jogo)):
            for j in range(len(jogo[i])):
                if jogo[i - 1][j - 1] == jogada:
                    if jogo[i - 1][j - 1] == '0' or jogo[i - 1][j - 1] == 'X':
                        print("Casa já ocupada")
                        jogou = False
                    else:
                        jogou = True
                        jogo[i - 1][j - 1] = 'X'
    return jogo


def substituir_por_o(jogo):
    jogou = False
    while jogou == False:
        print("Jogador 0")
        jogada = inserir_jogada(jogo)
        for i in range(len(jogo)):
            for j in range(len(jogo[i])):
                if jogo[i - 1][j - 1] == jogada:
                    if jogo[i - 1][j - 1] == '0' or jogo[i - 1][j - 1] == 'X':
                        print("Casa já ocupada")
                        jogou = False
                    else:
                        jogou = True
                        jogo[i - 1][j - 1] = '0'
    return jogo


def exibir_jogo(jogo):
    for vetor in jogo:
        print(vetor)


dimensao = 3

contador = 0
vencedor = ""

venceu = False
while venceu == False:
    for i in range(dimensao):
        contador = 0
        for j in range(dimensao):
            if jogo[i][j] == 'X':
                contador += 1
                if contador == dimensao:
                    venceu = True
                    print(f"X venceu em uma linha")

    for j in range(dimensao):
        contador = 0
        for i in range(dimensao):
            if jogo[i][j] == 'X':
                contador += 1
                if contador == dimensao:
                    venceu = True
                    print(f"X venceu em uma coluna")
    contador = 0
    for i in range(dimensao):
        if jogo[i][i] == 'X':
            contador += 1
            if contador == dimensao:
                venceu = True
                print('X venceu em uma diagonal')

    contador = 0
    for i in range(dimensao):
        if jogo[i][dimensao - i - 1] == 'X':
            contador += 1
            if contador == dimensao:
                venceu = True
                print('X venceu em uma diagonal')

    if venceu == False:
        exibir_jogo(jogo)
        jogada1 = substituir_por_x(jogo)
        if venceu == False:
            exibir_jogo(jogo)
            jogada2 = substituir_por_o(jogo)