print("minimo, maximo e soma total:")
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# print os numeros impares da lista
print("-="*15)
print("apenas numeros impares:")
odd_numbers = list(range(0, 20))
"""for x in odd_numbers:
    if x % 2 != 0:
        print(x)"""
impares = [x for x in odd_numbers if x%2!=0]
print(impares)
print("-="*15)
'''Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.'''
print("multiplos de 3:")
three = list(range(3,31))
'''for x in three:
    if x%3==0:
        print(x)'''
multiplos = [x for x in three if x%3==0]
print(three)
print("-="*15)
#cubos 
print("10 primeiros cubos:")
cubos = []
for valor in range(1,11):
    cubos.append(valor**3)
print(cubos)
print("-="*15)
#list comprehensions
print("modificando o exemplo anterior:")
cubos =[valor**3 for valor in range(1,11)]
print(cubos)

