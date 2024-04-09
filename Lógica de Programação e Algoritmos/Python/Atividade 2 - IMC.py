altura = float(input("Digite sua Altura: "))
peso = float(input("Digite seu Peso: "))

IMC = peso / (altura * altura)

print(f"O seu IMC é: {round(IMC, 2)}")

if IMC <= 30:
    print("Tudo Certo")
elif IMC >= 30:
    print("CUIDADO")

