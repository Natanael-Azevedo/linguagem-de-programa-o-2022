'''
Escreva um programa que recebe como entrada uma string contendo o nome completo de um aluno, funcionário ou professor da UFRN. Seu programa deverá gerar uma nova string contendo uma sugestão de novo login para seu usuário SIGAA. A sugestão de login deve ser construída a partir da seguinte operação: dado um nome completo, com nome e sobrenome (um ou mais), o login será sempre o primeiro nome e o último sobrenome separados pelo caractere ponto '.'

'''
nome = input()
lista = nome.split()
lista1 = lista[0:1]
lista2 = lista[-1:]
sugestao = f"{lista1[0]}.{lista2[-1]}"
print(sugestao.lower())