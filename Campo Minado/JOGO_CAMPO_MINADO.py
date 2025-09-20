# Santiago da Silva Rodrigues
# Caio Rezende Retto

import random

linhas = int(input("Escolha o tamanho do jogo: "))
bombas = linhas*3
largura = 2

def criar_tabuleiro(linhas):
    tabuleiro = [["_" for i in range(linhas)] for j in range(linhas)]
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if i == 0:
                tabuleiro[0][j] = j
            else:
                if j == 0:
                    tabuleiro[i][0] = i
                else:
                    tabuleiro[i][j] = "_"
    return tabuleiro

def inserir_bombas(tabuleiro):
    tabuleiro = criar_tabuleiro(linhas + 1)
    qtd_bombas = 0
    while qtd_bombas < bombas:
        linha = random.randint(0, len(tabuleiro) - 1)
        coluna = random.randint(0, len(tabuleiro) - 1)
        if tabuleiro[linha][coluna] == "_":
            tabuleiro[linha][coluna] = 'X'
            qtd_bombas += 1
    return tabuleiro

def inserir_jogada(linhas):
    pos1 = int(input("Digite a linha: "))
    pos2 = int(input("Digite a coluna: "))
    while 1 > pos1 > linhas or 1 > pos2 > linhas:
        print("Jogada inválida")
        pos1 = int(input("Digite a linha: "))
        pos2 = int(input("Digite a coluna: "))
    return pos1, pos2

def transforma_posicao(posicao):
    if posicao == '_' or posicao == "X":
        return '-'
    else:
        return posicao

def verificar_proximos(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] != "_":
        return
    else:
        direcoes = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        qtd_bombas_vizinhas = 0
        for d in direcoes:
            nova_linha, nova_coluna = linha + d[0], coluna + d[1]
            if 1 <= nova_linha <= linhas and 1 <= nova_coluna <= linhas:
                if tabuleiro[nova_linha][nova_coluna] == 'X':
                    qtd_bombas_vizinhas += 1

        if qtd_bombas_vizinhas == 0:
            tabuleiro[linha][coluna] = ' '
            for d in direcoes:
                nova_linha, nova_coluna = linha + d[0], coluna + d[1]
                if 1 <= nova_linha <= linhas and 1 <= nova_coluna <= linhas:
                    verificar_proximos(tabuleiro, nova_linha, nova_coluna)
        else:
            tabuleiro[linha][coluna] = qtd_bombas_vizinhas

def esconder_posicao(tabuleiro, esconder):
    for linha in tabuleiro:
        for posicao in linha:
            print(f"{esconder(posicao):<{largura}}", end=' ')
        print()

def revelar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for posicao in linha:
            print(f"{posicao:<{largura}}", end=' ')
        print()

def imprimir_com_marcacao(tabuleiro, marcacoes):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[i])):
            if (i, j) in marcacoes:
                print(f"{'Y':<{largura}}", end=' ')
            else:
                print(f"{transforma_posicao(tabuleiro[i][j]):<{largura}}", end=' ')
        print()

def verificar_vitoria(tabuleiro):
    for i in range(1, linhas + 1):
        for j in range(1, linhas + 1):
            if tabuleiro[i][j] == '_':
                return False
    return True

def jogar(linhas):
    tabuleiro = inserir_bombas(linhas)
    marcacoes = []
    fim = False
    # revelar_tabuleiro(tabuleiro)
    # esconder_posicao(tabuleiro, transforma_posicao)
    while fim == False:
        imprimir_com_marcacao(tabuleiro, marcacoes)
        linha, coluna = inserir_jogada(tabuleiro)
        opcao = int(input("Digite 1 para jogar \n"
                          "Digite 2 para marcar\n"
                          ""))
        if opcao == 1:
            if (linha, coluna) in marcacoes:
                marcacoes.remove((linha, coluna))
            if tabuleiro[linha][coluna] == "_":
                verificar_proximos(tabuleiro, linha, coluna)
            else:
                if tabuleiro[linha][coluna] == "X":
                    fim = True
                    print("Você acertou uma bomba!")
                    revelar_tabuleiro(tabuleiro)
            if verificar_vitoria(tabuleiro):
                print("Você venceu!")
                fim = True
        else:
            if (linha, coluna) in marcacoes:
                marcacoes.remove((linha, coluna))
            else:
                marcacoes.append((linha, coluna))



jogo = jogar(linhas)