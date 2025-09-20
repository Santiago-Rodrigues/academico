# Santiago da Silva Rodrigues
#Pedro Abrandes Condé

import random

palavra = ['sorteio', 'cachorro', 'algoritmo', 'dinamarca', 'estreito']
jogo = random.choice(palavra)

letras_palavra = []

for i in range(len(jogo)):
  if jogo[i] not in letras_palavra:
    letras_palavra.append(jogo[i])

# print(letras_palavra)
# print(jogo.upper())
espacos = len(jogo)
print(f'A palavra tem {espacos} letras')

vidas = 6
letras_corretas = []
letras_erradas = []


while vidas > 0:
  palavra_oculta = ""

  for i in jogo:
    if i in letras_corretas:
      palavra_oculta += " " + i
    else:
      palavra_oculta += " _ "
  print(f'Letras corretas: {letras_corretas}')
  print(f'Letras erradas: {letras_erradas}')
  print(f'Restam {vidas} vidas')

  if len(letras_corretas) == len(letras_palavra):
    vidas = 0
    print(f'Você venceu, a palavra é: {jogo.upper()}')
  else:
    print(f"Palavra: {palavra_oculta}")
    tentativa = input('\n'
                      'Escolha uma letra: ')

    if tentativa in jogo:
      if tentativa in letras_corretas:
        print('Letra já digitada')
      else:
        print("acertou")
        letras_corretas.append(tentativa)
  
    else:
      if tentativa in letras_erradas:
        print('Letra já digitada')
      else:
        print("errou")
        vidas -= 1
        letras_erradas.append(tentativa)
        
  
if vidas == 0:
  print('Fim de Jogo')
