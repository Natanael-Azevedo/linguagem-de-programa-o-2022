'''
Escreva um programa que lê quatro números inteiros, onde cada número será fornecido em uma linha separada.

O seu programa deve criar uma lista com esses números e em seguida remover dessa lista os dois menores elementos.

Ao final, imprima cada elemento da lista conforme abaixo.
'''
num=[]
for x in range(0,4):
    num.append(int(input()))
num.remove(min(num))
num.remove(min(num))

for i in num:
    print(i)
    