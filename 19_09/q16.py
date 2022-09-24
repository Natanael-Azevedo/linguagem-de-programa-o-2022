'''
Um número frequente é um número que aparece bastante (em listas, por exemplo), mas não sempre. Você deve escrever um programa para determinar se um certo número é frequente ou não.

O seu programa deve ler três listas de números e em seguida um número x. Em seguida, seu programa deve informar se x é um número frequente ou não. Considere que x é um número frequente se ele aparece em todas as listas de números menos uma.

Cada lista de números será fornecida em uma linha própria, onde cada número será separado por espaços. Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada 1:
1 2 3 4
5 6 7 8
4 6 8
4

- Exemplo de Saída 1:
4 é um número frequente


- Exemplo de Entrada 2:
10 20 30
10 100 1000
2 4 6 8 10
10

- Exemplo de Saída 2:
10 não é um número frequente
'''
l1 = input().split()
l2 = input().split()
l3 = input().split()
x = int(input())

if x in l1 and x in l2 and x in l3:
    print(f"{x} não é um número frequente")
else:
    print(f"{x} é um número frequente")