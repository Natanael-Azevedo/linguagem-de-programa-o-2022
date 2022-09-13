'''Escreva um programa que recebe como entrada uma sequência de 10 valores quaisquer. Seu programa deverá informar qual o maior e qual o menor  valor informado, além do MDC (máximo divisor comum) para estes dois valores. '''
lista = [255, 366, 201, 10, 15, 85, 998, 500, 144, 15]
# for x in range(10):
#   lista.append(int(input()))
lista.sort()
menor = lista[0]
maior = lista[-1]

x=1
for x in lista:
    if maior%x==0 and menor % x == 0:
        print(f'{maior} {menor} {x}')
        break
    else:
        x = x+1

print(f'{maior} {menor} {x}')
# 255 366 201 10 15 85 998 500 144 5
