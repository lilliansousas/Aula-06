notas = []
for i in range(1, 6):
    nota = float(input(f"Digite a sua nota aqui {i}:"))
    notas.append(nota)
    
media = sum(notas) / len(notas)
if media >= 6:
    classificacao = "Aprovado"
else:
    classificacao = "Reprovado"
print(f"\nMédia: {media:.2f}")
print(f"Classificação: {classificacao}")        