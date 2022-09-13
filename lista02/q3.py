"""Escreva um programa que receba do usuário duas listas de inteiros:
uma lista a com m elementos e outra lista b com n elementos. Seu
programa deverá gerar uma terceira lista c com m+n elementos, sendo
que os elementos de c serão os elementos de a e b inseridos de forma
alternada."""

m = int(input("entre com um numero: "))
lista_a = []
for x in range(m):
    lista_a.append(input())

n = int(input("entre com um numero: "))
lista_b = []
for x in range(n):
    lista_b.append(input())

lista_c = lista_a+lista_b
lista_c[::2]=lista_a
lista_c[1::2]=lista_b
print(lista_c)

'''
usando zip():
lista_c = list(itertools.chain(*zip(test_list1, test_list2))) 
print ("The interleaved list is : " + str(res)) 
'''