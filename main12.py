total = 0
for i in range(5):
    preco = float(input("Digite o preço do produto{}: ".format(i+1)))
    total += preco
    if total > 100:
        total *= 0.9
        print("Desconto aplicado!")
        break
    print("O total a pagar é:", total)