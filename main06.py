inicio = int(1)
fim = int(50)
soma_pares = 0

for numero in range(inicio,fim + 1):
    if numero % 2 == 0:
        soma_pares += numero

if soma_pares > 0:
    print("A soma dos numeros pares é:", soma_pares)
else:
    print("Não tem numeros pares dentro do intevalor")            
