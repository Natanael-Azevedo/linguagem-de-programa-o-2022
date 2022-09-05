"""
Pedro está fazendo uma viagem que passa por várias cidades.

Neste programa, você deve ler um número inteiro N e então ler o nome das N cidades que Pedro já visitou (o nome de cada cidade será fornecido em uma linha separada).

Em seguida, o seu programa deve imprimir a lista de cidades visitadas por Pedro de modo inverso, isto é, o nome da última cidade visitada deve ser impresso primeiro, depois o nome da penúltima cidade visitada e assim por diante.
"""
num = int(input())
cidades = []
for i in range(num):
    cidades.append(input())
    
cidades.reverse()
for x in cidades:
    print(x)