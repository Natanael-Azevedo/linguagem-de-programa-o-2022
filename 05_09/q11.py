'''
Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L1 com todos os números no intervalo de 1 até N.

Depois, o seu programa deve criar uma cópia L2 da lista L1 e ler mais dois valores inteiros, V1 e V2, da entrada.

O seu programa deve apagar da lista L1 os valores V1 e V2.

Ao final, imprima as listas L1 e L2 com o comando print.
'''
num = int(input())
lista_1 = []
for i in range(1,num+1):
    lista_1.append(i)

lista_2 = lista_1[:]
v1 = int(input())
v2 = int(input())

lista_1.remove(v1)
lista_1.remove(v2)

print(lista_1)
print(lista_2)