from os import remove
'''
Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L com todos os números ímpares no intervalo de 1 até N.

Depois, o seu programa deve ler dois valores inteiros, V1 e V2, da entrada e imprimir a soma dos elemento entre os índices V1 e V2 de L.

Por exemplo, no caso da lista [1, 3, 5, 7, 9], a soma dos elementos entre os índices 1 e 3 (a sublista [3, 5, 7]) é igual a 15.
'''

num = int(input())
odd = []
for i in range(1,num+1):
    if i % 2 != 0:
        odd.append(i)
print(odd)

v1 = int(input())
v2 = int(input())

soma = 0
for j in range(v1, v2+1):
  soma += odd[j]

print(soma)



