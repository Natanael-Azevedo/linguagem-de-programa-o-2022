import math

continuar = "sim"
pontos = []

# Lê pares de pontos do usuário
while continuar == "sim":
    x1 = float(input("Informe x1: "))
    y1 = float(input("Informe y1: "))
    x2 = float(input("Informe x2: "))
    y2 = float(input("Informe y2: "))
    pontos.append(((x1, y1), (x2, y2)))
    continuar = input("Deseja continuar (sim/não)? ")

# Calcula a distância entre cada par de pontos e imprime o resultado
maior_distancia = 0
pontos_mais_distantes = None

for p1, p2 in pontos:
    distancia = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    print(f"A distância entre {p1} e {p2} é {distancia}")
    
    if distancia > maior_distancia:
        maior_distancia = distancia
        pontos_mais_distantes = (p1, p2)

# Imprime o par de pontos mais distantes
print(f"O par de pontos mais distantes é {pontos_mais_distantes}, com distância {maior_distancia}")