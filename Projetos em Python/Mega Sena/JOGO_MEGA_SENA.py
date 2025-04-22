import random
# Santiago da Silva Rodrigues
# Caio Rezenze Retto

qtd_Numeros = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
valor_Aposta = [5, 35, 140, 420, 1050, 2310, 4620,8580, 15015, 25025, 40040, 61880, 92820, 135660, 193800]

# CONTROLE PARA SABER OS NÚMEROS SORTEADOS
# sorteio = []
# while len(sorteio) < 6:
#     gerar = random.randint(1, 60)
#     if gerar not in sorteio:
#         sorteio.append(gerar)
# print(sorteio)

valor = 0
qtd_Apostas = int(input('Digite a quantidade de apostas: '))
while valor == 0:
    if qtd_Apostas < 6 or qtd_Apostas > 20:
        valor = 0
        print("Aposta Inválida")
        qtd_Apostas = int(input('Digite a quantidade de apostas: '))
    else:
        for i in range(len(qtd_Numeros)):
            for j in range(len(valor_Aposta)):
                valor = (valor_Aposta[qtd_Apostas-6])
        print(f"Valor a ser pago: {valor},00")

        apostas = []
        while len(apostas) != qtd_Apostas:
            aposta = int(input('Digite suas apostas: '))
            if aposta < 1 or aposta > 60:
                print('Número inválido')
            else:
                if aposta in apostas:
                    print('Número já digitado, digite outro')
                else:
                    apostas.append(aposta)
        print(apostas)

        sorteio = []
        while len(sorteio) < 6:
            gerar = random.randint( 1,60)
            if gerar not in sorteio:
                sorteio.append(gerar)
        print(sorteio)

        premio = ''
        acertos = 0
        for a in range(len(apostas)):
            for b in range(len(sorteio)):
                if apostas[a]==sorteio[b]:
                    acertos += 1
        if acertos == 4:
            premio = 'Quadra'
        else:
            if acertos == 5:
                premio = 'Quina'
            else:
                if acertos == 6:
                    premio = 'Sena'

        print(f"Você acertou {acertos} números")
        if acertos > 4:
            print(f'Parabéns, você ganhou na {premio}')




