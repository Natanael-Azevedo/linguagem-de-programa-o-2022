'''Mostre dentre 3 valores informados pelo usuário, qual é o maior e qual é o menor'''
n1 = int(input())
n2 = int(input())
n3 = int(input())

maior = n1

if n2 > maior:
    maior = n2 
if n3 > maior:
    maior = n3 

menor = n1

if n2 < menor:
    menor = n2 
if n3 < menor:
    maior = n3

print(maior,menor)