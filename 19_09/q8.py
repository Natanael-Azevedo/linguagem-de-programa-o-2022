"""Escreva um programa que recebe as listas com os nomes dos alunos em três turmas de LiP. Em seguida, o seu programa deve ler um determinado nome e informar se em alguma turma há um aluno com o nome informado.

Cada lista de alunos em uma turma de LiP será fornecida em uma linha separada, onde os nomes dos alunos da turma são separados por uma vírgula. Veja o exemplo de entrada e saída abaixo.


- Exemplo de Entrada 1:
mateus,ana beatriz,julia,carlos
joão,carlos,lucas
alexandre,maria aparecida,zenaide
joão

- Exemplo de Saída 1:
Tem joão em alguma turma


- Exemplo de Entrada 2:
mateus,carlos,julia
joão,carlos,lucas
alexandre,maria,joão
marcos

- Exemplo de Saída 2:
Nenhuma turma tem marcos

# use split para formar uma lista a partir de uma linha da entrada
# turma = input().split(',')"""
turma = input()
turma_1=turma.split()
turma2 = input()
turma_2=turma.split()
turma3 = input()
turma_3=turma.split()
turma4 = turma_1+turma_2+turma_3



aluno = input()

if aluno in turma4:
        print(f"Tem {aluno} em alguma turma")
else:
        print(f"Nenhuma turma tem {aluno}")