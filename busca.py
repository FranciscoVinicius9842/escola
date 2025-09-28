numero = int(input("Digite um número impar (1-51): "))
lista = [1 , 3,  5, 7, 9, 11, 15, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51]
item = numero

baixo = 0
alto = len(lista) - 1

while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]

    print("Testando:", chute)

    if chute == item:
        print("Achei o número na posição", meio)
        break
    elif chute > item:
        alto = meio - 1
    else:
        baixo = meio + 1
else:
    print("Número não encontrado")