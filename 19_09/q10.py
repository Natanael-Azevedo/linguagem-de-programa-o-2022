"""Paolo fez uma pizza muito gostosa, com vários ingredientes. Porém, seu amigo Toni pediu para acrescentar mais alguns ingredientes na pizza. Você deve escrever um programa que adicionar os ingredientes de Toni à pizza, tomando cuidado para não adicionar um ingrediente mais de uma vez.

O seu programa deve ler uma lista dos ingredientes que Paolo usou na pizza e em seguida uma lista dos ingredientes que Toni quer adicionar.

Ao final, seu programa deve imprimir duas listas: uma lista com os ingredientes originais da pizza, e uma lista com a composição da pizza depois de adicionar os ingredientes que Toni pediu.

Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por vírgulas."""
pizza1 = input().split(',')
novos_ingd = input().split(',')

pizza3 = pizza1[:]

for ingrediente in novos_ingd:
    if ingrediente not in pizza3:
        pizza3.append(ingrediente)

print(pizza1)
print(pizza3)