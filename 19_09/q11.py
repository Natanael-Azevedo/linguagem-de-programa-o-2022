'''
Paolo fez uma pizza muito gostosa, com vários ingredientes. Seu amigo Toni também fez uma pizza e gostaria de saber se a pizza de Paolo possui todos os ingredientes que ele usou na sua própria pizza.

O seu programa deve ler uma lista dos ingredientes que Paolo usou na pizza e em seguida uma lista dos ingredientes que Toni usou.

Ao final, seu programa deve imprimir duas listas: uma indicando os ingredientes que os dois usaram e outra indicando os ingredientes que só Paolo usou.

Cada lista de ingredientes será fornecida em uma linha e os ingredientes serão separados por espaços.
'''
paolo = input().split()
toni = input().split()
apenas_p = paolo[:]
comum = []


for ingrediente in toni:
    if ingrediente in paolo:
        comum.append(ingrediente)

for x in toni:
    if x in apenas_p:
        apenas_p.remove(x)

print(comum)
print(apenas_p)