'''

Questão 4

Valor da questão: 1,00

Escreva um programa que lê quatro números inteiros, onde cada número será fornecido em uma linha separada.

O seu programa deve criar uma lista com esses números e em seguida remover dessa lista os dois maiores elementos.

Ao final, imprima a lista resultante com o comando print.
'''
num=[]
for x in range(0,4):
    num.append(int(input()))
    
num.remove(max(num))
num.remove(max(num))

print(num)