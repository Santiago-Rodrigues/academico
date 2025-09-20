# Jogo do Campo Minado

Uma versão em Python do clássico jogo de estratégia Campo Minado, com um tabuleiro de tamanho customizável.

## Como o Código Funciona

-   **`criar_tabuleiro(linhas)`**: Cria uma matriz (lista de listas) para representar o tabuleiro com o tamanho definido pelo usuário.
-   **`inserir_bombas(tabuleiro)`**: Distribui aleatoriamente um número de bombas ('X') pelo tabuleiro. A quantidade de bombas é calculada como `linhas * 3`.
-   **`inserir_jogada(linhas)`**: Captura e valida as coordenadas (linha e coluna) inseridas pelo jogador.
-   **`verificar_proximos(tabuleiro, linha, coluna)`**: Esta é a função central da lógica do jogo. Quando o jogador escolhe uma casa vazia:
    1.  Ela conta quantas bombas existem nas 8 casas vizinhas.
    2.  Se não houver bombas vizinhas, a casa se torna um espaço em branco (' ') e a função é chamada recursivamente para todas as casas vizinhas, revelando uma área segura.
    3.  Se houver bombas vizinhas, a casa revela o número de bombas adjacentes.
-   **Funções de Exibição**: Funções como `esconder_posicao` e `imprimir_com_marcacao` controlam como o tabuleiro é exibido para o jogador, ocultando as bombas e mostrando as marcações ('Y').
-   **`jogar(linhas)`**: É a função principal que controla o fluxo do jogo.
    1.  Inicializa o tabuleiro e as bombas.
    2.  Entra em um loop `while` que continua até o jogo acabar.
    3.  A cada turno, exibe o tabuleiro e pede ao jogador uma ação: "jogar" (revelar uma casa) ou "marcar" (sinalizar uma possível bomba).
    4.  Se o jogador revela uma bomba, o jogo termina com derrota.
    5.  Se o jogador revela todas as casas seguras, o jogo termina com vitória.

## Como Utilizar

1.  Execute o script: `python JOGO_CAMPO_MINADO.py`.
2.  Digite o tamanho desejado para o tabuleiro (ex: 10 para um tabuleiro 10x10).
3.  Digite as coordenadas da casa onde deseja jogar.
4.  Escolha a opção 1 para revelar a casa ou 2 para marcá-la com 'Y'.