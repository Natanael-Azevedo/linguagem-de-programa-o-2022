nome1 = input()
nome2 = input()
nome3 = input()

maior = nome1

if len(nome2) > len(maior):
    maior = nome2
if len(nome3) > len(maior):
    maior = nome3

print(maior)