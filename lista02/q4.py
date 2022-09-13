'''
Utilizando a abordagem de abrangência de listas, verifique qual o valor
que mais aparece em uma lista qualquer (escolha int, float ou string).
Imprima este valor e seu respectivo número de ocorrências. A lista
deverá ser informada pelo usuário do programa. Caso haja empate
entre valores, mostre todos estes valores. Um número não poderá ser
contado mais de uma vez.
Dica 1: para verificar se um valor está em uma lista
if valor in sua_lista:
#faça algo
#Ou not in para verificar se não está
Dica 2: sua_lista.count(value) retornar quantas vezes um número
aparece em uma lista
'''
import random

lista = [13, 14, 14, 15, 16, 14, 12, 17, 18,13,13,16]
lista.sort()
rep = 0
for x in range(0,len(lista)-1):
    if(lista[x]==lista[x+1]):
        rep +=1
        if(x==len(lista)-2):
             print(lista[x],',',rep)
    else:
        print(lista[x],',',rep)
        rep = 0