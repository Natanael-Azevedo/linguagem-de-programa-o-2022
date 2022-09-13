'''
Leia do teclado um valor inteiro n e em seguida uma sequência de n valores inteiros que representa a quantidade de nascimentos observados em uma cidade nos últimos n dias. Escreva um programa que imprima na tela o primeiro dia (índice da lista), excluindo-se o dia 0, em que se observa uma quantidade de nascimentos que é maior do que a soma de todos os nascimentos que o antecedem. 
Dica: Você pode usar a função enumerate para percorrer uma lista como mostrado na "Solução Inicial".  

lista = [45, 55, 65]
for indice, valor in enumerate(lista):
    print(f'O valor {valor} está no índice {indice}')
'''
num=int(input("entre com um número:"))
lista=[]
for x in range(num):
    lista.append(int(input()))
lista.remove[0]
for x in lista:
    if lista[1]>lista[0]:
        print("dia 1")
        break
    else:
        print("não há")
        break
