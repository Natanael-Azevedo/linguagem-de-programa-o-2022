'''Escreva um programa que recebe como entrada uma sequência de 10 valores quaisquer. Seu programa deverá informar qual o maior e qual o menor  valor informado, além do MDC (máximo divisor comum) para estes dois valores. '''
lista =[]
for x in range(10):
    lista.append(int(input()))   
lista.sort()
menor=lista[0]
maior=lista[-1]
resto = maior%menor
while(resto!=0):
    maior = menor
    menor = resto
    resto = maior%menor
    print(f'{maior} {menor} {resto}')

print(f'{maior} {menor} {resto}')
#255 366 201 10 15 85 998 500 144 5