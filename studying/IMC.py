n = int(input())
pessoas=[]
for x in range(n):
    nome = input("Nome:")
    peso = float(input("Peso:"))
    altura = float(input("Altura:"))
    tupla=(nome,peso,altura)
    pessoas.append(tupla)

#p=peso h=altura
for p in pessoas:
    for h in pessoas:
        imc = (p[1]/(h[2]**2))


if imc < 18.5:
	print(f"{pessoas[0]}(IMC={imc}) - Magreza leve")
elif imc < 25:
	print(f"{pessoas[0]}(IMC={imc}) - Saudável")
elif imc < 30:
	print(f"{pessoas[0]}(IMC={imc}) - Sobrepeso")
elif imc < 35:
	print(f"{pessoas[0]}(IMC={imc}) - Obesidade Grau I")
elif imc < 40:
	print(f"{pessoas[0]}(IMC={imc}) - Obesidade Grau II (severa)")
else:
	print(f"{pessoas[0]}(IMC={imc}) - Obesidade Grau III (mórbida)")