venda = int(input("Valor da venda: "))
pagamento = int(input("Valor pago: "))

if venda != pagamento:
    troco = pagamento - venda
    print(f"Tenha um bom dia, aqui esta seu troco {troco}")

    dez = int(troco/10)
    print(f"Notas de dez: {dez}")
    troco = troco/(dez*10)

    cinco = int(troco/5)
    print(f"Notas de cinco: {cinco}")
    troco = troco/(cinco*5)

    dois = int(troco/2)
    print(f"Notas de dois: {dois}")
    troco = troco/(dois*2)

    um = int(troco/1)
    print(f"Moedas de um: {um}")

else:
    print("Tenha um bom dia!")


