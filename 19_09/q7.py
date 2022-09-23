'''
Escreva um programa que lê três listas que especificam os ingredientes de diferentes saladas de frutas. Em seguida, o seu programa deve ler qual é a fruta favorita do usuário e imprimir uma mensagem informando se a fruta favorita do usuário ocorre em todas as saladas de frutas ou não.

Os ingredientes de cada salada de frutas serão fornecidos em uma linha própria, onde cada ingrediente de uma salada será separado por espaços. Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada 1:
banana maçã laranja mamão
uva banana manga
kiwi laranja pêssego banana
banana

- Exemplo de Saída 1:
banana aparece em todas as saladas


- Exemplo de Entrada 2:
banana maçã laranja mamão
goiaba uva banana manga
kiwi laranja pêssego
laranja

- Exemplo de Saída 2:
laranja não aparece em todas as saladas

# use split para formar uma lista a partir de uma linha da entrada
# salada = input().split()
'''
"""l1 = int(input())
lista1=[]
for x in range(l1):
    lista1.append(input().split())

l2 = int(input())
lista2=[]
for x in range(l2):
    lista2.append(input().split())

l3 = int(input())
lista3=[]
for x in range(l3):
    lista3.append(input().split())

fruta_favorita = input()

if fruta_favorita in lista1:
    if fruta_favorita in lista2:
       if fruta_favorita in lista3:
            print(f"{fruta_favorita} aparece em todas")
else:
    print(f"{fruta_favorita} não aparece em todas")"""

salada = input().split()
salada2 = input().split()
salada3 = input().split()

fruta_favorita = input()
if fruta_favorita in salada and fruta_favorita in salada2 and fruta_favorita in salada3:
    print(f"{fruta_favorita} aparece em todas as saladas")
else:
    print(f"{fruta_favorita} não aparece em todas as saladas")