# Jogo da Forca

Uma implementação em Python do popular jogo de adivinhação de palavras, o Jogo da Forca.

## Como o Código Funciona

-   **`palavra`**: Uma lista de palavras pré-definidas. A função `random.choice(palavra)` seleciona uma delas aleatoriamente para o jogo.
-   **`letras_palavra`**: Uma lista que armazena as letras únicas da palavra sorteada, usada para verificar a condição de vitória.
-   **Variáveis de Estado**:
    -   **`vidas`**: Controla o número de tentativas restantes do jogador (inicializado com 6).
    -   **`letras_corretas`**: Armazena as letras que o jogador acertou.
    -   **`letras_erradas`**: Armazena as letras que o jogador errou.
-   **Loop Principal (`while vidas > 0`)**: O jogo continua enquanto o jogador tiver vidas. A cada rodada:
    1.  Uma `palavra_oculta` é montada, exibindo as letras corretas e `_` para as letras ainda não adivinhadas.
    2.  O status do jogo (letras corretas, erradas e vidas restantes) é exibido.
    3.  O programa verifica se o jogador já acertou todas as letras. Se sim, exibe a mensagem de vitória e encerra o jogo.
    4.  O jogador insere uma letra. O programa verifica se a letra está na palavra secreta.
        -   Se estiver, e não tiver sido digitada antes, é adicionada a `letras_corretas`.
        -   Se não estiver, e não tiver sido digitada antes, o jogador perde uma vida e a letra é adicionada a `letras_erradas`.
-   O jogo termina quando o jogador vence ou quando as `vidas` chegam a 0.

## Como Utilizar

1.  Execute o script: `python JOGO_FORCA.py`.
2.  Adivinhe a palavra digitando uma letra por vez e pressionando Enter.