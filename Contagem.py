quantidade_notas = int(input("Quantas notas você deseja avaliar? "))
lista_notas = []
for contador in range(quantidade_notas):
    lista_notas.append(int(input("Digite a nota: ")))

quantidade_aprovados = 0
print("\n##### RESULTADO #####\n")
for nota in lista_notas:
    if nota >= 7:
        quantidade_aprovados += 1
        print("Nota " + str(nota) + ": aprovado.")
    else:
        print("Nota " + str(nota) + ": reprovado.")

print(f"A quantidade de aprovados foi {quantidade_aprovados}")
