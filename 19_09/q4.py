'''
Diz-se que um número primo p é primo de Sophie-Germain se 2p+1 também é primo. Implemente um programa que avalia um número inteiro informado pelo usuário, mostrando se ele é:
Primo de Sophie-Germain, ou;
Primo, ou;
Não primo.
'''
p = int(input())
s = (2*p+1)
mult=0
mult1=0

for count in range(2,p):
    if (p % count == 0):
        mult += 1
for count in range(2,s):
    if (s % count == 0):
        mult1 += 1
if(mult==0 and mult1==0):
    print("Numero primo de Sophie-Germain")
elif(mult==0):
    print("Numero primo")
else:
    print("Numero nao primo")