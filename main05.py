inicio = int(input("Digite o numero inicial:"))
fim = int(input("Digite o numero final:"))

soma_pare = 0
soma_impar = 0

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
        soma_pare += numero
        soma_impar += numero

    print("A soma dos numeros pares é:", soma_pare)
    print("A soma dos numeros impares é:", soma_impar)