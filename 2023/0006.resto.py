'''Calcule o resto de um divisao sem usar os operadores // % * /'''

x = int(input("Entre com um numero: "))
y = int(input("Entre com um numero: "))

while x >= y:
    x -= y
print(x)