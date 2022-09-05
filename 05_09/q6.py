'''
Escreva um programa que lê três números inteiros, onde cada número será fornecido em uma linha separada.

O seu programa deve criar uma lista com esses números e em seguida remover dessa lista o maior e o menor elemento.

Ao final, imprima o elemento restante conforme abaixo:
'''
num=[]

for x in range(0,3):
    num.append(int(input()))

num.remove(max(num))
num.remove(min(num))

print(num[0])