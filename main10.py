positivo = 0
negativo = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º numero: "))
    
    if numero == 0:
        print("Numero 0 encontrado. Interrompendo o programa.")
    elif numero > 0:
        positivo += 1
    else:
        negativo += 1
print(f"\nQuantidade de numeros positivos: {positivo}")
print(f"Quantidade de numeros negativos: {negativo}")                           