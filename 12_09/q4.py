num=int(input("entre com um número:"))
lista=[]
for x in range(num):
    lista.append(int(input()))
for indice, valor in enumerate(lista):
    print(f'O valor {valor} está no índice {indice}')