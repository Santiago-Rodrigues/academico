# Simulador da Mega Sena

Este script é um simulador de apostas da Mega Sena, onde o usuário pode escolher seus números e o programa realiza um sorteio para verificar os resultados.

## Como o Código Funciona

-   **`qtd_Numeros`** e **`valor_Aposta`**: Duas listas que armazenam a relação entre a quantidade de números apostados e o valor correspondente da aposta.
-   **Entrada do Usuário**: O programa primeiro pergunta a quantidade de números que o usuário deseja apostar (entre 6 e 20) e valida a entrada. Com base na quantidade, o valor a ser pago é exibido.
-   **Coleta das Apostas**: Um loop `while` coleta as apostas do usuário, garantindo que os números estejam entre 1 e 60 e que não haja números repetidos.
-   **Sorteio**: O programa utiliza `random.randint(1, 60)` para gerar 6 números aleatórios e únicos, simulando o sorteio da Mega Sena.
-   **Verificação de Acertos**: O código compara a lista de números apostados pelo usuário com a lista de números sorteados. Um contador `acertos` armazena a quantidade de números correspondentes.
-   **Resultado**: Ao final, o programa exibe a quantidade de acertos e, caso o usuário tenha acertado 4, 5 ou 6 números, exibe uma mensagem de parabéns indicando se ganhou na "Quadra", "Quina" ou "Sena".

## Como Utilizar

1.  Execute o script: `python JOGO_MEGA_SENA.py`.
2.  Digite a quantidade de números que deseja apostar.
3.  Digite cada um dos seus números de aposta.
4.  O programa exibirá os números sorteados e o seu resultado.