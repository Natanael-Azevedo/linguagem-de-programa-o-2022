'''
Escreva um programa que lê o nome de 3 pessoas, onde cada nome será fornecido em uma linha separada.

O seu programa deve criar uma lista com o comprimento desses nomes e imprimir a lista resultante com o comando print.

'''
names=[]
for x in range(0,3):
    names.append(input())

tamanhos=[]
for i in names:
    tamanhos.append(len(i))
print(tamanhos)

