'''
Implemente um programa para calcular e mostrar o teto de um conjunto de n valores positivos informados pelo usuário. 
'''
n = int(input())
num = []
for x in range(n):
    y=float(input())
    z = int(y)
    if y-z!=0:
       z+=1
    else: 
        y=z
    num.append(z)
for x in num:
    print (x, end=" ")