'''
Leia do teclado um valor inteiro n e em seguida uma sequência de n valores inteiros que representa a quantidade de nascimentos observados em uma cidade nos últimos n dias. Escreva um programa que imprima na tela o primeiro dia (índice da lista), excluindo-se o dia 0, em que se observa uma quantidade de nascimentos que é maior do que a soma de todos os nascimentos que o antecedem. 
Dica: Você pode usar a função enumerate para percorrer uma lista como mostrado na "Solução Inicial".  

lista = [45, 55, 65]
for indice, valor in enumerate(lista):
    print(f'O valor {valor} está no índice {indice}')
'''
lista=[]
n=int(input())
for num in range(n):
  num=int(input())
  lista.append(num)
soma=0
for indice, valor in enumerate(lista):
    if indice>0:
      if valor> soma:
        print(f"dia {indice}")
        break
      elif indice == n-1:
        print("não há")
    soma+=valor    