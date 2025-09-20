# Jogo da Velha

Este script implementa o clássico Jogo da Velha em Python, executado diretamente no terminal.

## Como o Código Funciona

O jogo é controlado por uma série de funções que gerenciam o estado do tabuleiro e as jogadas dos jogadores.

-   **`jogo`**: Uma matriz 3x3 que representa o tabuleiro, inicializada com números de 1 a 9 para indicar as posições.
-   **`inserir_jogada(jogo)`**: Solicita ao jogador que digite a linha e a coluna desejada. A função valida se a entrada está dentro dos limites do tabuleiro (1 a 3).
-   **`substituir_por_x(jogo)`** e **`substituir_por_o(jogo)`**: Estas funções gerenciam o turno de cada jogador ('X' e 'O'). Elas chamam a função `inserir_jogada` e verificam se a casa escolhida já está ocupada. Caso esteja livre, a posição é atualizada com a marcação do jogador.
-   **`exibir_jogo(jogo)`**: Imprime o estado atual do tabuleiro no terminal.
-   **Loop Principal**: O coração do jogo. Após cada jogada, um loop verifica todas as condições de vitória possíveis:
    -   Verifica as três linhas.
    -   Verifica as três colunas.
    -   Verifica as duas diagonais.
-   O jogo alterna entre os jogadores até que uma das condições de vitória seja atendida.

## Como Utilizar

1.  Execute o script em um terminal com Python: `python JOGO_VELHA.py`.
2.  Quando for sua vez, digite o número da linha (1, 2 ou 3) e da coluna (1, 2 ou 3) para fazer sua jogada.