import math
'''
As coordenadas (x, y) de um ponto no plano podem ser armazenadas em uma tupla, como mostrado abaixo:
    ponto1 = (10.4, 5.5)
Salve em uma lista um conjunto de n tuplas, representando n pontos informados pelo usuário. Mostre na tela quais são os dois pontos deste conjunto que apresentam a maior distância entre si. A distância entre dois pontos é dado pela Norma Euclidiana
'''
n = int(input())
pontos = []
maior = 0

for num in range(n):
    x = float(input())
    y = float(input())
    tupla = (x,y)
    pontos.append(tupla)
for p1 in range(len(pontos)):
    for p2 in range(len(pontos)):
        distancia = math.sqrt((pontos[p2][0]-pontos[p1][0])**2+(pontos[p2][1]-pontos[p1][1])**2)
        if distancia > maior:
            P1=pontos[p1]
            P2=pontos[p2]
print(f'Mais distantes: {P1} {P2}')