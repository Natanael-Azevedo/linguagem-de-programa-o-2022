'''
Crie um programa que exibe se um dia é dia 'útil', 'fim de semana' ou 'dia inválido', dado o número referente ao dia. Considere que domingo é o dia 1 e sábado é o dia 7.
'''
dia = int(input())
if dia>=2 and dia<=6:
    print("Dia util")
if dia==1 or dia==7:
    print("Fim de semana")
if dia>7:
     print("Dia invalido")