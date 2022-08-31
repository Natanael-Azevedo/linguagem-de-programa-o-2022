# Elabore um algoritmo que receba como
# entrada o valor do saque realizado pelo
# cliente de um banco e retorne quantas notas
# de cada valor serão necessárias para atender
# ao saque com a menor quantidade de notas
# possível. Serão utilizadas notas de 100, 50,
# 73
# possível. Serão utilizadas notas de 100, 50,
# 20, 10, 5, 2 e 1 reais.
saque = 388

cem = int(saque/100)
print(cem)
saque = saque - (cem*100)
cinquenta = int(saque/50)
print(cinquenta)
saque = saque - (cinquenta*50)
vinte = int(saque/20)
print(vinte)
saque = saque - (vinte*20)
dez = int(saque/10)
print(dez)
saque = saque - (dez*10)
cinco = int(saque/5)
print(cinco)
saque = saque - (cinco*5)
um = saque
print(um)
