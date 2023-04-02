
frasco = int(input("Quantos ml tem sua garrafa ?: "))
padrao = 0
acionamentos = 0


while(frasco>padrao):
    padrao = padrao + 200
    acionamentos = acionamentos + 1

if padrao > frasco:
    acionamentos -= 1

print(acionamentos)




