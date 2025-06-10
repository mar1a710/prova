nota = float(input("Digite a nota: "))
if nota >= 0 and nota <= 10:
    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Nota inválida")