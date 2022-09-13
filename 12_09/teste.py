lista = [255, 366, 201, 10, 15, 85, 998, 500, 144, 5]
# for x in range(10):
#   lista.append(int(input()))
lista.sort()
menor = lista[0]
maior = lista[-1]
nova_lista=[maior,menor]

for x in lista:
    if nova_lista % x == 0:
        print(f'{maior} {menor} {x}')
        break
    else:
        x = x+1

print(f'{maior} {menor} {x}')
# 255 366 201 10 15 85 998 500 144 5
