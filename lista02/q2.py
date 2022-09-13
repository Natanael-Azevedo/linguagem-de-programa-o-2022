n = int(input("Informe n: "))
lista = []
for x in range(n):
    lista.append(float(input("Informe um valor: ")))
lista.sort()
len_lista = len(lista)
if len_lista % 2 == 0:
    print(lista[len_lista//2-1]+lista[len_lista//2])
else:
    print(lista[len_lista//2])