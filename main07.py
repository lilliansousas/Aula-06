palavra = input("Digite qualquer palavra que você quise:").lower()

contador_vogais = 0

vogais = 'aeiou'

for letra in palavra:
    if letra in vogais:
        contador_vogais += 1
    
print(f"O numero de vogais na palavra'{palavra}' é:{contador_vogais}")