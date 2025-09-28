# escola
Programa em Python que faz uma busca binária em uma lista de números ímpares entre 1 e 51.

O usuário deve digitar um número ímpar no intervalo de 1 a 51. O programa então procura esse número dentro de uma lista ordenada. A cada passo, ele testa o número que está no meio da lista:

Se for igual ao número digitado, o programa informa a posição em que o número foi encontrado.

Se o número digitado for menor que o do meio, a busca continua na metade da esquerda da lista.

Se o número digitado for maior, a busca continua na metade da direita da lista.

Caso o número não esteja na lista, o programa informa que não encontrou.

Esse método é mais rápido do que verificar todos os elementos um por um, porque reduz a lista de busca pela metade a cada comparação.