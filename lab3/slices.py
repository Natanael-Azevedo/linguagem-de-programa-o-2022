#list comprehensions

print("modificando o exemplo anterior:")
cubos =[valor**3 for valor in range(1,11)]
print(cubos)
print(f"Esses são os 3 primeiro números da lista:{cubos[0:3]}")
print(f"Esses são os números do meio da lista:{cubos[5:8]}")
print(f"Esses são os ultimos números da lista:{cubos[7:]}")