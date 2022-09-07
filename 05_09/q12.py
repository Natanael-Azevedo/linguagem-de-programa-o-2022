'''
Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista com todos os números pares positivos menores do que N.

O seu programa deve então percorrer essa lista e imprimir cada elemento dela com o comando print.
'''
num = int(input())
par = []
for i in range(1,num):
    if i<num and i%2==0:
        par.append(i)
for x in par:
    print(x)