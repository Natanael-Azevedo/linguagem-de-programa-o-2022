
venda = int(input("Total da compra:"))
pagamento = int(input("Quanto o cliente pagou:"))
if venda != pagamento:
    troco = pagamento - venda
    print(f"Tenha um bom dia e volte sempre, troco:{troco}")
    cem = int(troco/100)
    print("notas de cem: {cem}")
    troco = troco - (cem*100)

    cinquenta = int(troco/50)
    print(cinquenta)
    troco = troco - (cinquenta*50)

    vinte = int(troco/20)
    print(vinte)
    troco = troco - (vinte*20)
    dez = int(troco/10)

    print(dez)
    troco = troco - (dez*10)
    cinco = int(troco/5)

    print(cinco)
    troco = troco - (cinco*5)
    um = troco

    print(um)
    
else:
    print("Tenha um bom dia e volte sempre!")