'''
Pedro está fazendo uma viagem que passa por várias cidades. Neste programa, você deve ler um número inteiro N e então ler o nome das N cidades que Pedro já visitou (o nome de cada cidade será fornecido em uma linha separada).

Em seguida, o seu programa deve imprimir a lista de cidades visitadas por Pedro em ordem alfabética.
'''

num = int(input())
cidades = []
for i in range(num):
    cidades.append(input())
cidades.sort()
for x in cidades:
    print(x)